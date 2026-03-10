<template>
  <header class="header">
    <div class="container header__content">
      <div class="header__info">
        <div class="header__picandname">
          <div class="header__pic">
            <img src="@/assets/images/sl.jpg" class="header__picavatar" alt="Sébastien LEMOINE">
          </div>
          <div class="header__name">
            <h1 class="header__title">Sébastien LEMOINE</h1>
            <p class="header__subtitle">Responsable Pédagogique | Leadership & Stratégie Éducative</p>
          </div>
        </div>
      </div>
      <nav class="nav">
        <ul class="nav__list">
          <li class="nav__item" v-for="(link, index) in navLinks" :key="index">
            <router-link 
              :to="link.path" 
              class="nav__link"
              :class="{ 
                'nav__link--ancor': link.isAncor,
                'active': isActive(link)
              }"
              @click="handleClick(link)"
            >
              {{ link.text }}
            </router-link>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const navLinks = ref([
  { text: 'À propos', path: '/#about', isAncor: true },
  { text: 'Compétences', path: '/#competences', isAncor: true },
  { text: 'Articles récents', path: '/#blog', isAncor: true },
  { text: 'Contact', path: '/#contact', isAncor: true },
  { text: '|', path: '#', isAncor: false },
  { text: 'Tous les articles', path: '/blog', isAncor: false }
])

const activeSection = ref('about')

const isActive = (link) => {
  if (link.isAncor) {
    return activeSection.value === link.path.split('#')[1]
  }
  return route.path === link.path
}

const handleClick = (link) => {
  if (!link.isAncor) {
    // Si ce n'est pas un lien d'ancrage, on réinitialise la section active
    activeSection.value = ''
  }
}

const updateActiveSection = () => {
  const sections = document.querySelectorAll('section[id]')
  const headerHeight = document.querySelector('.header').offsetHeight
  const scrollPosition = window.scrollY + headerHeight
  const windowHeight = window.innerHeight
  const documentHeight = document.documentElement.scrollHeight

  sections.forEach((section, index) => {
    const sectionTop = section.offsetTop - headerHeight
    const sectionHeight = section.offsetHeight

    // Pour la dernière section (Contact)
    if (index === sections.length - 1) {
      // Si on est proche du bas de la page, on considère que la section Contact est active
      if (scrollPosition + windowHeight >= documentHeight - 100) {
        activeSection.value = section.id
      }
    } else if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
      activeSection.value = section.id
    }
  })
}

onMounted(() => {
  window.addEventListener('scroll', updateActiveSection)
  updateActiveSection() // Initial check
})

onUnmounted(() => {
  window.removeEventListener('scroll', updateActiveSection)
})
</script> 