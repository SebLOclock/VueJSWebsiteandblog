<template>
  <IntersectionObserver>
    <section id="contact" class="section">
      <h2 class="section__title">Échangeons</h2>
      <div class="contact-container">
        <div class="contact-info">
          <p class="contact-intro">Envie de discuter pédagogie, tech, numérique responsable, ou tout simplement d'échanger ? N'hésitez pas.</p>
          <p>
            <i class="fas fa-envelope"></i>
            <a href="mailto:lemoine.sebastien.cdf@gmail.com">lemoine.sebastien.cdf@gmail.com</a>
          </p>
          <p>
            <i class="fab fa-linkedin"></i>
            <a href="https://linkedin.com/in/sébastien-lemoine-679b3b52" target="_blank">
              LinkedIn
            </a>
          </p>
          <p>
            <i class="fab fa-bluesky"></i>
            <a href="https://bsky.app/profile/sebastienlemoine.bsky.social" target="_blank">
              Bluesky
            </a>
          </p>
          <p>
            <i class="fas fa-map-marker-alt"></i>
            Compiègne, France
          </p>
        </div>
      </div>
    </section>
  </IntersectionObserver>
</template>

<script setup>
import IntersectionObserver from './IntersectionObserver.vue'
</script> 