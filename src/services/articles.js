import { marked } from 'marked'
import fm from 'front-matter'

// Import all markdown files at build time
const articleFiles = import.meta.glob('@/content/articles/*.md', {
  query: '?raw',
  import: 'default',
  eager: true
})

function parseArticle(raw) {
  const { attributes, body } = fm(raw)
  return {
    ...attributes,
    content: marked(body)
  }
}

// Parse and sort all articles by date (newest first)
const allArticles = Object.values(articleFiles)
  .map(parseArticle)
  .sort((a, b) => new Date(b.date) - new Date(a.date))

export function getArticles(limit) {
  return limit ? allArticles.slice(0, limit) : allArticles
}

export function getArticleBySlug(slug) {
  return allArticles.find(a => a.slug === slug) || null
}
