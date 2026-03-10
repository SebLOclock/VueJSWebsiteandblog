<template>
  <IntersectionObserver>
    <section id="competences" class="section">
      <h2 class="section__title">Ce que j'apporte</h2>
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
  'Leadership & intelligence collective': 'fa-brain',
  'Gestion de projets': 'fa-tasks',
  'Formation & montée en compétences': 'fa-graduation-cap',
  'Sécurité numérique': 'fa-shield-halved',
  'Éducation au numérique': 'fa-chalkboard-user',
  'Intelligence artificielle': 'fa-robot',
  'Sensibilisation parents & familles': 'fa-people-roof',
  'Architecture logicielle': 'fa-code',
  'Développement web': 'fa-code-branch',
  'Veille tech & innovation': 'fa-lightbulb',
  'Vulgarisation & transmission': 'fa-comments'
}

const competenceGroups = ref([
  {
    title: 'Accompagner les équipes',
    items: [
      'Gestion d\'équipe',
      'Leadership & intelligence collective',
      'Gestion de projets',
      'Formation & montée en compétences'
    ]
  },
  {
    title: 'Protéger et éduquer',
    items: [
      'Sécurité numérique',
      'Éducation au numérique',
      'Intelligence artificielle',
      'Sensibilisation parents & familles'
    ]
  },
  {
    title: 'Construire et transmettre',
    items: [
      'Architecture logicielle',
      'Développement web',
      'Veille tech & innovation',
      'Vulgarisation & transmission'
    ]
  }
])
</script> 