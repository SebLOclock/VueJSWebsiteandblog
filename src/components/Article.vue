<template>
  <article id="article" class="section">
    <div v-if="!article" class="error">
      Article non trouvé
    </div>
    <template v-else>
      <div v-if="article.image" class="article__image-container">
        <img
          :src="article.image"
          :alt="article.title"
          class="article__image"
        >
      </div>

      <div class="article__meta">
        <h1 class="article__title">{{ article.title }}</h1>
        <div class="article__meta-info">
          <p class="article__date">{{ formatDate(article.date) }}</p>
          <p class="article__author">{{ article.author }}</p>
        </div>
      </div>

      <div class="article__content-container">
        <div class="article__content" v-html="article.content"></div>
      </div>

      <RecentArticles />
    </template>
  </article>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { getArticleBySlug } from '@/services/articles'
import RecentArticles from './RecentArticles.vue'

const route = useRoute()
const article = ref(getArticleBySlug(route.params.slug))

const formatDate = (date) => {
  return new Date(date).toLocaleDateString()
}

watch(
  () => route.params.slug,
  (newSlug) => {
    if (newSlug) {
      article.value = getArticleBySlug(newSlug)
    }
  }
)
</script>

<style scoped>
.error {
  text-align: center;
  padding: 2rem;
  color: #dc3545;
  font-size: 1.2rem;
}

.article__meta-info {
  display: flex;
  gap: 1rem;
  align-items: center;
  color: #666;
  font-size: 0.9rem;
}
</style>
