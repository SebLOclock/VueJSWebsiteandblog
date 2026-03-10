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
  margin-top: 4rem;
  padding-top: 4rem;
  border-top: 1px solid #eee;
}

.recent-articles__empty {
  text-align: center;
  padding: 2rem;
  color: #666;
}

.blog-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  padding: 0 1rem;
}

.blog-post {
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.blog-post:hover {
  transform: translateY(-5px);
}

.blog-post__image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.blog-post__title {
  font-size: 1.2rem;
  margin: 1rem;
  color: #333;
  line-height: 1.4;
}

.blog-post__description {
  margin: 0 1rem;
  color: #666;
  font-size: 0.9rem;
  line-height: 1.6;
}

.blog-post__date {
  margin: 1rem;
  color: #666;
  font-size: 0.9rem;
}

.blog-post__link {
  display: inline-block;
  margin: 1rem;
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.blog-post__link:hover {
  background-color: #0056b3;
}

@media (max-width: 768px) {
  .blog-container {
    grid-template-columns: 1fr;
  }
}
</style>
