<template>
  <footer class="footer">
    <div class="container">
      <p>&copy; {{ currentYear }} Sébastien LEMOINE. Tous droits réservés.</p>
    </div>
  </footer>
</template>

<script setup>
import { computed } from 'vue'

const currentYear = computed(() => new Date().getFullYear())
</script> 