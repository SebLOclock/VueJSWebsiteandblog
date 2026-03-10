<template>
  <section class="recent-articles">
    <h2 class="section__title">Articles récents</h2>
    <div v-if="loading" class="recent-articles__loading">
      Chargement des articles récents...
    </div>
    <div v-else-if="error" class="recent-articles__error">
      {{ error }}
    </div>
    <div v-else-if="filteredArticles.length === 0" class="recent-articles__empty">
      Aucun autre article récent disponible
    </div>
    <div v-else class="blog-container">
      <article v-for="article in filteredArticles" :key="article.id" class="blog-post">
        <img 
          :src="article._embedded['wp:featuredmedia'][0].source_url" 
          :alt="article.title.rendered"
          class="blog-post__image"
        >
        <h3 class="blog-post__title" v-html="cleanText(article.title.rendered)"></h3>
        <p class="blog-post__description" v-html="article.excerpt.rendered"></p>
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
import { ref, onMounted, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { fetchPosts } from '@/services/api'
import DOMPurify from 'dompurify'

const route = useRoute()
const articles = ref([])
const loading = ref(true)
const error = ref(null)

const cleanText = (text) => {
  return DOMPurify.sanitize(text)
    .replace(/&rsquo;/g, "'")
    .replace(/&quot;/g, '"')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
}

const formatDate = (date) => {
  return new Date(date).toLocaleDateString()
}

// Filtrer les articles pour exclure l'article actuel
const filteredArticles = computed(() => {
  return articles.value.filter(article => article.slug !== route.params.slug)
})

const loadArticles = async () => {
  try {
    loading.value = true
    error.value = null
    articles.value = await fetchPosts(4) // Récupérer 4 articles pour avoir 3 après filtrage
  } catch (err) {
    error.value = err.message
    console.error('Erreur lors du chargement des articles récents :', err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadArticles()
})

// Recharger les articles quand la route change
watch(
  () => route.params.slug,
  () => {
    loadArticles()
  }
)
</script>

<style scoped>
.recent-articles {
  margin-top: 4rem;
  padding-top: 4rem;
  border-top: 1px solid #eee;
}

.recent-articles__loading,
.recent-articles__error,
.recent-articles__empty {
  text-align: center;
  padding: 2rem;
  color: #666;
}

.recent-articles__error {
  color: #dc3545;
}

/* Réutilisation des styles du composant Blog */
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