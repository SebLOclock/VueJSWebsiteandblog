<template>
  <main class="main container">
    <section class="section">
      <h2 class="section__title">Tous les articles</h2>
      <div class="blog-list">
        <article v-for="post in posts" :key="post.id" class="blog-list__item">
          <img 
            :src="post._embedded['wp:featuredmedia'][0].source_url" 
            :alt="post.title.rendered"
            class="blog-list__image"
          >
          <div class="blog-list__content">
            <h3 class="blog-list__title" v-html="cleanText(post.title.rendered)"></h3>
            <p class="blog-list__description" v-html="post.excerpt.rendered"></p>
            <div class="blog-list__meta">
              <span class="blog-list__date">{{ formatDate(post.date) }}</span>
              <span class="blog-list__author">{{ post._embedded.author[0].name }}</span>
            </div>
            <router-link 
              :to="{ name: 'article', params: { slug: post.slug }}"
              class="blog-list__link"
            >
              Lire la suite
            </router-link>
          </div>
        </article>
      </div>
    </section>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchPosts } from '@/services/api'
import DOMPurify from 'dompurify'

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
    posts.value = await fetchPosts(100)
  } catch (error) {
    console.error('Erreur lors du chargement des articles :', error)
  }
})
</script> 