<template>
  <main class="main container">
    <div class="not-found">
      <h1>404 - Page non trouvée</h1>
      <p>La page que vous recherchez n'existe pas ou a été déplacée.</p>
      <router-link to="/" class="btn">Retour à l'accueil</router-link>
    </div>
  </main>
</template>

<script setup>
// Pas de logique nécessaire
</script>

<style scoped>
.not-found {
  text-align: center;
  padding: 6rem 2rem;
}

.not-found h1 {
  font-family: var(--heading-font);
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: var(--primary-color);
}

.not-found p {
  font-size: 1.1rem;
  color: var(--light-text);
  margin-bottom: 2.5rem;
}

.btn {
  display: inline-block;
  padding: 14px 32px;
  background-color: var(--primary-color);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.95rem;
  transition: var(--transition);
  letter-spacing: 0.02em;
}

.btn:hover {
  background-color: var(--secondary-color);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(26, 35, 50, 0.2);
}
</style> 