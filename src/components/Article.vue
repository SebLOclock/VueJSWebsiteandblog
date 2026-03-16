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
          loading="lazy"
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
import { ref, watch, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useHead } from '@unhead/vue'
import { getArticleBySlug } from '@/services/articles'
import RecentArticles from './RecentArticles.vue'

const route = useRoute()
const article = ref(getArticleBySlug(route.params.slug))

const formatDate = (date) => {
  return new Date(date).toLocaleDateString()
}

const siteUrl = 'https://sebastienlemoine.fr'

const pageTitle = computed(() =>
  article.value ? `${article.value.title} | Sébastien LEMOINE` : 'Article non trouvé'
)
const pageDescription = computed(() =>
  article.value?.excerpt || ''
)
const pageUrl = computed(() =>
  `${siteUrl}/article/${article.value?.slug || ''}`
)
const pageImage = computed(() =>
  article.value?.image ? `${siteUrl}${article.value.image}` : ''
)

useHead({
  title: pageTitle,
  meta: [
    { name: 'description', content: pageDescription },
    { property: 'og:title', content: pageTitle },
    { property: 'og:description', content: pageDescription },
    { property: 'og:type', content: 'article' },
    { property: 'og:url', content: pageUrl },
    { property: 'og:image', content: pageImage },
    { property: 'og:locale', content: 'fr_FR' },
    { property: 'og:site_name', content: 'Sébastien LEMOINE' },
    { property: 'article:author', content: 'Sébastien LEMOINE' },
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:title', content: pageTitle },
    { name: 'twitter:description', content: pageDescription },
    { name: 'twitter:image', content: pageImage },
  ],
  link: [
    { rel: 'canonical', href: pageUrl },
  ],
  script: [
    {
      type: 'application/ld+json',
      innerHTML: computed(() => article.value ? JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'BlogPosting',
        headline: article.value.title,
        description: article.value.excerpt,
        image: article.value.image ? `${siteUrl}${article.value.image}` : undefined,
        datePublished: article.value.date,
        url: `${siteUrl}/article/${article.value.slug}`,
        author: {
          '@type': 'Person',
          name: 'Sébastien LEMOINE',
          url: 'https://sebastienlemoine.fr',
        },
        publisher: {
          '@type': 'Person',
          name: 'Sébastien LEMOINE',
          url: 'https://sebastienlemoine.fr',
        },
        mainEntityOfPage: {
          '@type': 'WebPage',
          '@id': `${siteUrl}/article/${article.value.slug}`,
        },
      }) : '{}'),
    },
  ],
})

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
