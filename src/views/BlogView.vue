<template>
  <main class="main container">
    <section class="section">
      <h2 class="section__title">Tous les articles</h2>
      <div class="blog-list">
        <article v-for="post in posts" :key="post.slug" class="blog-list__item">
          <img
            v-if="post.image"
            :src="post.image"
            :alt="post.title"
            class="blog-list__image"
          >
          <div class="blog-list__content">
            <h3 class="blog-list__title">{{ post.title }}</h3>
            <p class="blog-list__description">{{ post.excerpt }}</p>
            <div class="blog-list__meta">
              <span class="blog-list__date">{{ formatDate(post.date) }}</span>
              <span class="blog-list__author">{{ post.author }}</span>
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
import { getArticles } from '@/services/articles'

const posts = getArticles()

const formatDate = (date) => {
  return new Date(date).toLocaleDateString()
}
</script>
