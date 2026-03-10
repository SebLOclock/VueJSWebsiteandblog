<template>
  <div ref="target" :class="{ 'active': isIntersecting }">
    <slot></slot>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  threshold: {
    type: Number,
    default: 0.5
  },
  rootMargin: {
    type: String,
    default: '-50% 0px'
  }
})

const target = ref(null)
const isIntersecting = ref(false)
let observer = null

onMounted(() => {
  observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        isIntersecting.value = entry.isIntersecting
      })
    },
    {
      threshold: props.threshold,
      rootMargin: props.rootMargin
    }
  )

  if (target.value) {
    observer.observe(target.value)
  }
})

onUnmounted(() => {
  if (observer && target.value) {
    observer.unobserve(target.value)
  }
})
</script> 