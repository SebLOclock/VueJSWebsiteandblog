#!/usr/bin/env python3
"""
Récupère visits.csv par FTP et génère un rapport Markdown.

Configuration via variables d'environnement :
  FTP_HOST     hôte FTP
  FTP_USER     utilisateur
  FTP_PASS     mot de passe
  FTP_PATH     chemin du fichier CSV (défaut : /logs/visits.csv)

Usage :
  export FTP_HOST=ftp.example.com FTP_USER=user FTP_PASS=pass
  python3 scripts/fetch-visits.py
"""

import csv
import io
import os
import sys
from collections import Counter
from datetime import datetime
from ftplib import FTP, all_errors


def connect_and_download():
    host = os.environ.get("FTP_HOST")
    user = os.environ.get("FTP_USER")
    password = os.environ.get("FTP_PASS")
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
        row["date_day"] = row["date"][:10]
        rows.append(row)
    return rows


def generate_report(rows):
    if not rows:
        return "# Rapport de visites\n\nAucune visite enregistrée.\n"

    total = len(rows)
    unique_visitors = len({row["ip_hash"] for row in rows})

    visits_per_slug = Counter(row["slug"] for row in rows)
    visits_per_day = Counter(row["date_day"] for row in rows)
    unique_per_slug = {}
    for row in rows:
        unique_per_slug.setdefault(row["slug"], set()).add(row["ip_hash"])

    first_day = min(visits_per_day)
    last_day = max(visits_per_day)

    lines = []
    lines.append(f"# Rapport de visites")
    lines.append(f"")
    lines.append(f"Période : **{first_day}** au **{last_day}**")
    lines.append(f"Total visites : **{total}** | Visiteurs uniques : **{unique_visitors}**")
    lines.append(f"")

    # Top articles
    lines.append("## Top articles")
    lines.append("")
    lines.append("| # | Article | Visites | Uniques |")
    lines.append("|---|---------|---------|---------|")
    for rank, (slug, count) in enumerate(visits_per_slug.most_common(), 1):
        uniq = len(unique_per_slug[slug])
        lines.append(f"| {rank} | {slug} | {count} | {uniq} |")
    lines.append("")

    # Visites par article
    lines.append("## Visites par article")
    lines.append("")
    lines.append("| Article | Visites | Uniques |")
    lines.append("|---------|---------|---------|")
    for slug in sorted(visits_per_slug):
        count = visits_per_slug[slug]
        uniq = len(unique_per_slug[slug])
        lines.append(f"| {slug} | {count} | {uniq} |")
    lines.append("")

    # Visites par jour
    lines.append("## Visites par jour")
    lines.append("")
    lines.append("| Date | Visites |")
    lines.append("|------|---------|")
    for day in sorted(visits_per_day):
        lines.append(f"| {day} | {visits_per_day[day]} |")
    lines.append("")

    return "\n".join(lines)


def main():
    content = connect_and_download()
    rows = parse_csv(content)
    report = generate_report(rows)

    report_path = os.path.join(os.path.dirname(__file__), "..", "visits-report.md")
    report_path = os.path.normpath(report_path)

    with open(report_path, "w") as f:
        f.write(report)

    print(report)
    print(f"\n--- Rapport sauvegardé dans {report_path}")


if __name__ == "__main__":
    main()
