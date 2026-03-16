<template>
  <IntersectionObserver>
    <section id="competences" class="section">
      <h2 class="section__title">Ce que j'apporte</h2>
      <div class="competences-container">
        <div v-for="(group, index) in competenceGroups" :key="index" class="competences-group">
          <h3>{{ group.title }}</h3>
          <p class="competence-description">{{ group.description }}</p>
        </div>
      </div>
    </section>
  </IntersectionObserver>
</template>

<script setup>
import { ref } from 'vue'
import IntersectionObserver from './IntersectionObserver.vue'

const competenceGroups = ref([
  {
    title: 'Donner les clés du numérique',
    description: 'Le numérique, ça devrait pas être réservé à ceux qui ont fait 5 ans d\'études en info. J\'accompagne les équipes, les profs, les parents, tous ceux qui veulent comprendre sans qu\'on leur parle comme à des idiots. Mon boulot, c\'est de transformer le jargon en quelque chose d\'utile et de concret. Pas de slides à rallonge, pas de bullshit : juste les bonnes clés pour être autonome.'
  },
  {
    title: 'Protéger sans faire peur',
    description: 'La cybersécurité, c\'est pas réservé aux mecs en sweat à capuche dans un sous-sol. Fuites de données, arnaques en ligne, IA qui dérape : j\'explique les vrais risques aux pros, aux parents, aux enseignants. Sans dramatiser, sans infantiliser. L\'idée c\'est que vous sachiez quoi faire, pas que vous ayez la trouille.'
  },
  {
    title: 'Construire et transmettre',
    description: 'Je code, j\'architecture, je fais de la veille. Mais ce qui me passionne le plus, c\'est de transmettre. Vulgariser la tech pour qu\'elle ne soit plus réservée à ceux qui parlent couramment le JSON. Si c\'est clair pour ma nièce de 8 ans, c\'est que c\'est bon.'
  }
])
</script>
