<template>
  <IntersectionObserver>
    <section id="competences" class="section">
      <h2 class="section__title">Compétences Clés</h2>
      <div class="competences-container">
        <div v-for="(group, index) in competenceGroups" :key="index" class="competences-group">
          <h3>{{ group.title }}</h3>
          <ul class="competence-list">
            <li v-for="(competence, compIndex) in group.items" :key="compIndex" class="competence-item">
              <i :class="['fas', competenceIcons[competence] || 'fa-check', 'competence-icon']"></i>
              <span class="competence-text">{{ competence }}</span>
            </li>
          </ul>
        </div>
      </div>
    </section>
  </IntersectionObserver>
</template>

<script setup>
import { ref } from 'vue'
import IntersectionObserver from './IntersectionObserver.vue'

const competenceIcons = {
  'Gestion d\'équipe': 'fa-users',
  'Leadership situationnel': 'fa-star',
  'Gestion de projets': 'fa-tasks',
  'Intelligence collective': 'fa-brain',
  'Stratégie Éducative': 'fa-graduation-cap',
  'Transformation Digitale': 'fa-digital-tachograph',
  'Innovation pédagogique': 'fa-lightbulb',
  'Veille technologique': 'fa-magnifying-glass-chart',
  'Architecture logicielle': 'fa-code',
  'Développement web': 'fa-code-branch',
  'Méthodes agiles': 'fa-sync',
  'Intelligence artificielle': 'fa-robot'
}

const competenceGroups = ref([
  {
    title: 'Management & Leadership',
    items: [
      'Gestion d\'équipe',
      'Leadership situationnel',
      'Gestion de projets',
      'Intelligence collective'
    ]
  },
  {
    title: 'Stratégie & Innovation',
    items: [
      'Stratégie Éducative',
      'Transformation Digitale',
      'Innovation pédagogique',
      'Veille technologique'
    ]
  },
  {
    title: 'Technique & Développement',
    items: [
      'Architecture logicielle',
      'Développement web',
      'Méthodes agiles',
      'Intelligence artificielle'
    ]
  }
])
</script> 