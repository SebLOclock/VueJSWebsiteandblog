<template>
  <IntersectionObserver>
    <section id="blog" class="section">
      <h2 class="section__title">Dernières réflexions</h2>
      <div class="blog-container">
        <article v-for="post in posts" :key="post.slug" class="blog-post">
          <img
            v-if="post.image"
            :src="post.image"
            :alt="post.title"
            class="blog-post__image"
          >
          <h3 class="blog-post__title">{{ post.title }}</h3>
          <p class="blog-post__description">{{ post.excerpt }}</p>
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
import { getArticles } from '@/services/articles'
import IntersectionObserver from './IntersectionObserver.vue'

const posts = getArticles(3)

const formatDate = (date) => {
  return new Date(date).toLocaleDateString()
}
</script>
