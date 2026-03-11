<template>
  <section class="recent-articles">
    <h2 class="section__title">Articles récents</h2>
    <div v-if="filteredArticles.length === 0" class="recent-articles__empty">
      Aucun autre article récent disponible
    </div>
    <div v-else class="blog-container">
      <article v-for="article in filteredArticles" :key="article.slug" class="blog-post">
        <img
          v-if="article.image"
          :src="article.image"
          :alt="article.title"
          class="blog-post__image"
          loading="lazy"
        >
        <h3 class="blog-post__title">{{ article.title }}</h3>
        <p class="blog-post__description">{{ article.excerpt }}</p>
        <p class="blog-post__date">{{ formatDate(article.date) }}</p>
        <router-link
          :to="{ name: 'article', params: { slug: article.slug }}"
          class="blog-post__link"
        >
          Lire la suite
        </router-link>
      </article>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { getArticles } from '@/services/articles'

const route = useRoute()
const articles = getArticles(4)

const formatDate = (date) => {
  return new Date(date).toLocaleDateString()
}

const filteredArticles = computed(() => {
  return articles.filter(a => a.slug !== route.params.slug)
})
</script>

<style scoped>
.recent-articles {
  margin-top: 5rem;
  padding-top: 4rem;
  border-top: 1px solid rgba(26, 35, 50, 0.08);
}

.recent-articles__empty {
  text-align: center;
  padding: 2rem;
  color: var(--light-text);
}

.blog-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.blog-post {
  background: var(--card-background);
  border-radius: var(--border-radius);
  overflow: hidden;
  border: 1px solid rgba(26, 35, 50, 0.06);
  transition: var(--transition);
  display: flex;
  flex-direction: column;
}

.blog-post:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(26, 35, 50, 0.1);
  border-color: rgba(201, 169, 110, 0.2);
}

.blog-post__image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.blog-post__title {
  font-family: var(--heading-font);
  font-size: 1.15rem;
  margin: 20px 24px 10px;
  color: var(--primary-color);
  line-height: 1.4;
  font-weight: 600;
}

.blog-post__description {
  margin: 0 24px;
  color: var(--light-text);
  font-size: 0.9rem;
  line-height: 1.6;
  flex-grow: 1;
}

.blog-post__date {
  margin: 16px 24px 8px;
  color: var(--light-text);
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.blog-post__link {
  display: inline-flex;
  align-items: center;
  margin: 0 24px 24px;
  color: var(--accent-color);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  transition: var(--transition);
}

.blog-post__link:hover {
  color: var(--primary-color);
}

.blog-post__link::after {
  content: '→';
  margin-left: 6px;
  transition: var(--transition);
}

.blog-post__link:hover::after {
  transform: translateX(4px);
}

@media (max-width: 768px) {
  .blog-container {
    grid-template-columns: 1fr;
  }
}
</style>
