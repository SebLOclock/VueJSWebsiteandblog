<template>
  <main class="main container">
    <About />
    <Competences />
    <Blog />
    <Contact />
  </main>
</template>

<script setup>
import { useHead } from '@unhead/vue'
import About from '@/components/About.vue'
import Competences from '@/components/Competences.vue'
import Blog from '@/components/Blog.vue'
import Contact from '@/components/Contact.vue'

useHead({
  title: 'Sébastien LEMOINE | Pédagogie, Tech & Numérique Responsable',
  meta: [
    { name: 'description', content: 'Sébastien LEMOINE, Ingénieur pédagogique spécialisé en IA, éducation numérique et sécurité en ligne. Décryptage tech honnête et accessible pour parents, profs et curieux.' },
    { property: 'og:title', content: 'Sébastien LEMOINE | Pédagogie, Tech & Numérique Responsable' },
    { property: 'og:description', content: 'Ingénieur pédagogique spécialisé en IA, éducation numérique et sécurité en ligne. Décryptage tech honnête et accessible.' },
    { property: 'og:type', content: 'website' },
    { property: 'og:url', content: 'https://sebastienlemoine.fr/' },
    { property: 'og:locale', content: 'fr_FR' },
    { property: 'og:site_name', content: 'Sébastien LEMOINE' },
    { name: 'twitter:card', content: 'summary' },
    { name: 'twitter:title', content: 'Sébastien LEMOINE | Pédagogie, Tech & Numérique Responsable' },
    { name: 'twitter:description', content: 'Ingénieur pédagogique spécialisé en IA, éducation numérique et sécurité en ligne.' },
  ],
  link: [
    { rel: 'canonical', href: 'https://sebastienlemoine.fr/' },
  ],
  script: [
    {
      type: 'application/ld+json',
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'Person',
        name: 'Sébastien LEMOINE',
        url: 'https://sebastienlemoine.fr',
        jobTitle: 'Ingénieur pédagogique',
        description: 'Spécialisé en IA, éducation numérique et sécurité en ligne. 10 ans à parler de tech de façon honnête et accessible.',
        sameAs: [
          'https://linkedin.com/in/sébastien-lemoine-679b3b52',
          'https://bsky.app/profile/sebastienlemoine.bsky.social',
        ],
        knowsAbout: [
          'Intelligence artificielle',
          'Pédagogie numérique',
          'Sécurité en ligne',
          'Éducation numérique',
        ],
      }),
    },
  ],
})
</script>
