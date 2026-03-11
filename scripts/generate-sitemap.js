const fs = require('fs')
const path = require('path')
const fm = require('front-matter')

const siteUrl = 'https://sebastienlemoine.fr'
const distDir = path.join(__dirname, '../dist')
const articlesDir = path.join(__dirname, '../src/content/articles')

// Lire tous les articles et extraire slug + date
const articles = fs.readdirSync(articlesDir)
  .filter(f => f.endsWith('.md'))
  .map(f => {
    const raw = fs.readFileSync(path.join(articlesDir, f), 'utf-8')
    const { attributes } = fm(raw)
    return { slug: attributes.slug, date: attributes.date }
  })
  .sort((a, b) => new Date(b.date) - new Date(a.date))

const today = new Date().toISOString().split('T')[0]

const urls = [
  { loc: '/', lastmod: today, priority: '1.0' },
  { loc: '/blog', lastmod: articles[0]?.date || today, priority: '0.8' },
  ...articles.map(a => ({
    loc: `/article/${a.slug}`,
    lastmod: a.date,
    priority: '0.7',
  })),
]

const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map(u => `  <url>
    <loc>${siteUrl}${u.loc}</loc>
    <lastmod>${u.lastmod}</lastmod>
    <priority>${u.priority}</priority>
  </url>`).join('\n')}
</urlset>
`

fs.writeFileSync(path.join(distDir, 'sitemap.xml'), sitemap)
console.log(`Sitemap généré avec ${urls.length} URLs`)
