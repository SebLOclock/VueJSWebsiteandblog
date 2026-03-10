<template>
  <article id="article" class="section">
    <div v-if="loading" class="loading">
      Chargement de l'article...
    </div>
    <div v-else-if="error" class="error">
      {{ error }}
    </div>
    <template v-else-if="article._embedded">
      <div class="article__image-container">
        <img 
          :src="article._embedded['wp:featuredmedia'][0].source_url" 
          :alt="article.title.rendered"
          class="article__image"
        >
      </div>
      
      <div class="article__meta">
        <h1 class="article__title" v-html="article.title.rendered"></h1>
        <div class="article__meta-info">
          <p class="article__date">{{ formatDate(article.date) }}</p>
          <p class="article__author">{{ article._embedded.author[0].name }}</p>
          <p v-if="views !== null" class="article__views">{{ views }} vues</p>
        </div>
      </div>
      
      <div class="article__content-container">
        <div class="article__content" v-html="article.content.rendered"></div>
      </div>

      <RecentArticles />
    </template>
    <div v-else class="error">
      Article non trouvé
    </div>
  </article>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { fetchPostBySlug, incrementPostViews } from '@/services/api'
import DOMPurify from 'dompurify'
import RecentArticles from './RecentArticles.vue'

const route = useRoute()
const article = ref({})
const loading = ref(true)
const error = ref(null)
const views = ref(null)

const formatDate = (date) => {
  return new Date(date).toLocaleDateString()
}

const loadArticle = async (slug) => {
  try {
    loading.value = true
    error.value = null
    views.value = null
    
    
    if (!slug) {
      throw new Error('Slug non fourni')
    }
    
    article.value = await fetchPostBySlug(slug)
    if (!article.value) {
      throw new Error('Article non trouvé')
    }
    
    // Incrémenter le compteur de vues
    try {
      const viewsData = await incrementPostViews(article.value.id)
      views.value = viewsData.views
    } catch (viewsError) {
      console.error('Erreur lors de l\'incrémentation des vues:', viewsError)
      // Ne pas bloquer l'affichage de l'article si l'incrémentation échoue
    }
    
  } catch (err) {
    error.value = err.message
    console.error('Erreur lors du chargement de l\'article :', err)
  } finally {
    loading.value = false
  }
}

// Charger l'article initial
onMounted(() => {
  loadArticle(route.params.slug)
})

// Observer les changements de route
watch(
  () => route.params.slug,
  (newSlug) => {
    if (newSlug) {
      loadArticle(newSlug)
    }
  }
)
</script>

<style scoped>
.loading {
  text-align: center;
  padding: 2rem;
  font-size: 1.2rem;
  color: #666;
}

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

.article__views {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.article__views::before {
  content: "👁";
  font-size: 1.1em;
}
</style> 