<template>
  <IntersectionObserver>
    <section id="blog" class="section">
      <h2 class="section__title">Articles</h2>
      <div class="blog-container">
        <article v-for="post in posts" :key="post.id" class="blog-post">
          <img 
            :src="post._embedded['wp:featuredmedia'][0].source_url" 
            :alt="post.title.rendered"
            class="blog-post__image"
          >
          <h3 class="blog-post__title" v-html="cleanText(post.title.rendered)"></h3>
          <p class="blog-post__description" v-html="post.excerpt.rendered"></p>
          <p class="blog-post__date">{{ formatDate(post.date) }}</p>
          <router-link 
            :to="{ name: 'article', params: { slug: post.slug }}"
            class="blog-post__link"
          >
            Lire la suite
          </router-link>
        </article>
      </div>
    </section>
  </IntersectionObserver>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchPosts } from '@/services/api'
import DOMPurify from 'dompurify'
import IntersectionObserver from './IntersectionObserver.vue'

const posts = ref([])

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

onMounted(async () => {
  try {
    posts.value = await fetchPosts(3)
  } catch (error) {
    console.error('Erreur lors du chargement des articles :', error)
  }
})
</script> 