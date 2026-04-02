#!/usr/bin/env python3
"""
Récupère visits.csv par FTP et génère une page HTML interactive de statistiques.

Les données brutes sont embarquées en JSON dans la page.
Le filtrage par période se fait côté client (JavaScript).

Configuration via variables d'environnement :
  FTP_HOST     hôte FTP
  FTP_USER     utilisateur
  FTP_PASS     mot de passe
  FTP_PATH     chemin du fichier CSV (défaut : /logs/visits.csv)

Usage :
  export FTP_HOST=ftp.example.com FTP_USER=user FTP_PASS=pass
  python3 scripts/generate-stats-html.py
"""

import csv
import io
import json
import os
import sys
from datetime import datetime
from ftplib import FTP, all_errors


def connect_and_download():
    host = os.environ.get("FTP_HOST", "ftp.cluster121.hosting.ovh.net")
    user = os.environ.get("FTP_USER", "vnhhzud")
    password = os.environ.get("FTP_PASS", "Sikouillansky06100901")
    remote_path = os.environ.get("FTP_PATH", "/www/logs/visits.csv")

    if not all([host, user, password]):
        print("Erreur : FTP_HOST, FTP_USER et FTP_PASS doivent être définis.", file=sys.stderr)
        sys.exit(1)

    try:
        ftp = FTP(host)
        ftp.login(user, password)
    except all_errors as e:
        print(f"Erreur de connexion FTP : {e}", file=sys.stderr)
        sys.exit(1)

    buf = io.BytesIO()
    try:
        ftp.retrbinary(f"RETR {remote_path}", buf.write)
    except all_errors as e:
        print(f"Erreur lors du téléchargement de {remote_path} : {e}", file=sys.stderr)
        ftp.quit()
        sys.exit(1)

    ftp.quit()
    return buf.getvalue().decode("utf-8")


def parse_csv(content):
    reader = csv.DictReader(io.StringIO(content))
    rows = []
    for row in reader:
        rows.append({
            "date": row["date"][:10],
            "slug": row["slug"],
            "ip_hash": row["ip_hash"],
        })
    return rows


def generate_html(rows, generated_at):
    data_json = json.dumps(rows, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Statistiques du blog</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary-color: #1a2332;
            --secondary-color: #2d3748;
            --accent-color: #c9a96e;
            --accent-light: #f0e6d3;
            --text-color: #1a1a2e;
            --light-text: #6b7280;
            --background-color: #fafaf8;
            --card-background: #ffffff;
            --border-radius: 12px;
            --box-shadow: 0 2px 20px rgba(26, 35, 50, 0.06);
            --heading-font: 'Playfair Display', Georgia, serif;
            --body-font: 'Inter', -apple-system, sans-serif;
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: var(--body-font);
            line-height: 1.7;
            color: var(--text-color);
            background-color: var(--background-color);
            -webkit-font-smoothing: antialiased;
        }}

        .container {{
            max-width: 960px;
            margin: 0 auto;
            padding: 40px 24px;
        }}

        h1 {{
            font-family: var(--heading-font);
            font-size: 2rem;
            color: var(--primary-color);
            margin-bottom: 8px;
        }}

        .subtitle {{
            color: var(--light-text);
            font-size: 0.9rem;
            margin-bottom: 24px;
        }}

        /* Filtres */
        .filters {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            align-items: center;
            margin-bottom: 32px;
        }}

        .filter-btn {{
            padding: 8px 16px;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            background: var(--card-background);
            color: var(--light-text);
            font-family: var(--body-font);
            font-size: 0.85rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .filter-btn:hover {{
            border-color: var(--accent-color);
            color: var(--text-color);
        }}

        .filter-btn.active {{
            background: var(--primary-color);
            color: #fff;
            border-color: var(--primary-color);
        }}

        .filter-sep {{
            width: 1px;
            height: 24px;
            background: #e5e7eb;
            margin: 0 4px;
        }}

        .date-input {{
            padding: 7px 12px;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            font-family: var(--body-font);
            font-size: 0.85rem;
            color: var(--text-color);
            background: var(--card-background);
        }}

        .date-input:focus {{
            outline: none;
            border-color: var(--accent-color);
        }}

        .date-label {{
            font-size: 0.8rem;
            color: var(--light-text);
        }}

        /* Cartes KPI */
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 16px;
            margin-bottom: 40px;
        }}

        .kpi-card {{
            background: var(--card-background);
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 24px;
            text-align: center;
        }}

        .kpi-value {{
            font-family: var(--heading-font);
            font-size: 2.2rem;
            font-weight: 700;
            color: var(--primary-color);
        }}

        .kpi-label {{
            font-size: 0.8rem;
            color: var(--light-text);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 4px;
        }}

        /* Sections */
        .section {{
            background: var(--card-background);
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 28px;
            margin-bottom: 24px;
        }}

        .section h2 {{
            font-family: var(--heading-font);
            font-size: 1.3rem;
            color: var(--primary-color);
            margin-bottom: 20px;
            padding-bottom: 12px;
            border-bottom: 2px solid var(--accent-light);
        }}

        /* Tableaux */
        table {{
            width: 100%;
            border-collapse: collapse;
        }}

        th {{
            text-align: left;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--light-text);
            padding: 8px 12px;
            border-bottom: 1px solid #e5e7eb;
        }}

        td {{
            padding: 10px 12px;
            border-bottom: 1px solid #f3f4f6;
            font-size: 0.9rem;
        }}

        tr:last-child td {{
            border-bottom: none;
        }}

        .rank {{
            color: var(--accent-color);
            font-weight: 700;
            width: 40px;
        }}

        .num {{
            text-align: right;
            font-weight: 600;
            font-variant-numeric: tabular-nums;
            white-space: nowrap;
            width: 80px;
        }}

        th.num {{
            text-align: right;
        }}

        .slug-name {{
            font-weight: 500;
            margin-bottom: 4px;
        }}

        .date-cell {{
            font-variant-numeric: tabular-nums;
            white-space: nowrap;
            width: 110px;
        }}

        .bar-td {{
            width: 100%;
        }}

        /* Barres */
        .bar-container {{
            background: #f3f4f6;
            border-radius: 4px;
            height: 8px;
            overflow: hidden;
        }}

        .bar {{
            height: 100%;
            border-radius: 4px;
            background: linear-gradient(90deg, var(--accent-color), #d4b87a);
            min-width: 4px;
            transition: width 0.3s ease;
        }}

        .bar-daily {{
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
        }}

        .empty-state {{
            text-align: center;
            padding: 40px 20px;
            color: var(--light-text);
        }}

        /* Footer */
        .footer {{
            text-align: center;
            color: var(--light-text);
            font-size: 0.8rem;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e5e7eb;
        }}

        @media (max-width: 600px) {{
            .container {{ padding: 20px 16px; }}
            h1 {{ font-size: 1.5rem; }}
            .kpi-value {{ font-size: 1.8rem; }}
            .section {{ padding: 20px; }}
            .filters {{ gap: 6px; }}
            .filter-btn {{ padding: 6px 12px; font-size: 0.8rem; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Statistiques du blog</h1>
        <p class="subtitle">Généré le {generated_at}</p>

        <div class="filters">
            <button class="filter-btn active" data-range="all">Tout</button>
            <button class="filter-btn" data-range="7">7 jours</button>
            <button class="filter-btn" data-range="14">14 jours</button>
            <button class="filter-btn" data-range="30">30 jours</button>
            <button class="filter-btn" data-range="90">90 jours</button>
            <div class="filter-sep"></div>
            <span class="date-label">Du</span>
            <input type="date" class="date-input" id="date-from">
            <span class="date-label">au</span>
            <input type="date" class="date-input" id="date-to">
        </div>

        <div class="kpi-grid">
            <div class="kpi-card">
                <div class="kpi-value" id="kpi-total">0</div>
                <div class="kpi-label">Visites totales</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-value" id="kpi-uniques">0</div>
                <div class="kpi-label">Visiteurs uniques</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-value" id="kpi-articles">0</div>
                <div class="kpi-label">Articles</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-value" id="kpi-days">0</div>
                <div class="kpi-label">Jours actifs</div>
            </div>
        </div>

        <div class="section">
            <h2>Top articles</h2>
            <table>
                <thead>
                    <tr>
                        <th></th>
                        <th>Article</th>
                        <th class="num">Visites</th>
                        <th class="num">Uniques</th>
                    </tr>
                </thead>
                <tbody id="table-articles"></tbody>
            </table>
            <div class="empty-state" id="empty-articles" hidden>Aucune visite sur cette période.</div>
        </div>

        <div class="section">
            <h2>Visites par jour</h2>
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th></th>
                        <th class="num">Visites</th>
                    </tr>
                </thead>
                <tbody id="table-daily"></tbody>
            </table>
            <div class="empty-state" id="empty-daily" hidden>Aucune visite sur cette période.</div>
        </div>

        <div class="footer">
            Données issues du tracking anonymisé &mdash; aucune donnée personnelle collectée
        </div>
    </div>

    <script>
    const RAW_DATA = {data_json};

    const $ = (sel) => document.querySelector(sel);
    const $$ = (sel) => document.querySelectorAll(sel);

    function slugToTitle(slug) {{
        return slug.replace(/-/g, ' ').replace(/^./, c => c.toUpperCase());
    }}

    function filterRows(from, to) {{
        return RAW_DATA.filter(r => r.date >= from && r.date <= to);
    }}

    function computeStats(rows) {{
        const total = rows.length;
        const uniqueIps = new Set(rows.map(r => r.ip_hash));
        const slugs = {{}};
        const days = {{}};

        for (const r of rows) {{
            if (!slugs[r.slug]) slugs[r.slug] = {{ visits: 0, ips: new Set() }};
            slugs[r.slug].visits++;
            slugs[r.slug].ips.add(r.ip_hash);

            days[r.date] = (days[r.date] || 0) + 1;
        }}

        const topArticles = Object.entries(slugs)
            .map(([slug, d]) => ({{ slug, visits: d.visits, uniques: d.ips.size }}))
            .sort((a, b) => b.visits - a.visits);

        const daily = Object.entries(days)
            .map(([date, visits]) => ({{ date, visits }}))
            .sort((a, b) => a.date.localeCompare(b.date));

        return {{
            total,
            uniqueVisitors: uniqueIps.size,
            articleCount: topArticles.length,
            dayCount: daily.length,
            topArticles,
            daily,
        }};
    }}

    function render(stats) {{
        $('#kpi-total').textContent = stats.total;
        $('#kpi-uniques').textContent = stats.uniqueVisitors;
        $('#kpi-articles').textContent = stats.articleCount;
        $('#kpi-days').textContent = stats.dayCount;

        // Top articles
        const tbody = $('#table-articles');
        const emptyA = $('#empty-articles');
        if (stats.topArticles.length === 0) {{
            tbody.innerHTML = '';
            emptyA.hidden = false;
            return;
        }}
        emptyA.hidden = true;
        const maxVisits = stats.topArticles[0].visits;
        tbody.innerHTML = stats.topArticles.map((a, i) => {{
            const pct = (a.visits / maxVisits * 100).toFixed(0);
            return `<tr>
                <td class="rank">#${{i + 1}}</td>
                <td>
                    <div class="slug-name">${{slugToTitle(a.slug)}}</div>
                    <div class="bar-container"><div class="bar" style="width:${{pct}}%"></div></div>
                </td>
                <td class="num">${{a.visits}}</td>
                <td class="num">${{a.uniques}}</td>
            </tr>`;
        }}).join('');

        // Visites par jour
        const tbodyD = $('#table-daily');
        const emptyD = $('#empty-daily');
        if (stats.daily.length === 0) {{
            tbodyD.innerHTML = '';
            emptyD.hidden = false;
            return;
        }}
        emptyD.hidden = true;
        const maxDaily = Math.max(...stats.daily.map(d => d.visits));
        tbodyD.innerHTML = stats.daily.map(d => {{
            const pct = (d.visits / maxDaily * 100).toFixed(0);
            return `<tr>
                <td class="date-cell">${{d.date}}</td>
                <td class="bar-td"><div class="bar-container"><div class="bar bar-daily" style="width:${{pct}}%"></div></div></td>
                <td class="num">${{d.visits}}</td>
            </tr>`;
        }}).join('');
    }}

    // Bornes globales
    const allDates = RAW_DATA.map(r => r.date).sort();
    const globalMin = allDates[0];
    const globalMax = allDates[allDates.length - 1];

    const inputFrom = $('#date-from');
    const inputTo = $('#date-to');
    inputFrom.min = globalMin;
    inputFrom.max = globalMax;
    inputTo.min = globalMin;
    inputTo.max = globalMax;

    function today() {{
        return new Date().toISOString().slice(0, 10);
    }}

    function daysAgo(n) {{
        const d = new Date();
        d.setDate(d.getDate() - n + 1);
        return d.toISOString().slice(0, 10);
    }}

    function applyRange(from, to) {{
        inputFrom.value = from;
        inputTo.value = to;
        const rows = filterRows(from, to);
        render(computeStats(rows));
    }}

    // Boutons preset
    $$('.filter-btn').forEach(btn => {{
        btn.addEventListener('click', () => {{
            $$('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const range = btn.dataset.range;
            if (range === 'all') {{
                applyRange(globalMin, globalMax);
            }} else {{
                applyRange(daysAgo(parseInt(range)), today());
            }}
        }});
    }});

    // Dates custom
    function onDateChange() {{
        $$('.filter-btn').forEach(b => b.classList.remove('active'));
        const from = inputFrom.value || globalMin;
        const to = inputTo.value || globalMax;
        const rows = filterRows(from, to);
        render(computeStats(rows));
    }}
    inputFrom.addEventListener('change', onDateChange);
    inputTo.addEventListener('change', onDateChange);

    // Init : tout afficher
    applyRange(globalMin, globalMax);
    </script>
</body>
</html>"""


def main():
    content = connect_and_download()
    rows = parse_csv(content)

    if not rows:
        print("Aucune visite enregistrée.", file=sys.stderr)
        sys.exit(0)

    generated_at = datetime.now().strftime("%d/%m/%Y à %H:%M")
    html = generate_html(rows, generated_at)

    output_path = os.path.join(os.path.dirname(__file__), "..", "stats.html")
    output_path = os.path.normpath(output_path)

    with open(output_path, "w") as f:
        f.write(html)

    print(f"Page de statistiques générée : {output_path}")


if __name__ == "__main__":
    main()
