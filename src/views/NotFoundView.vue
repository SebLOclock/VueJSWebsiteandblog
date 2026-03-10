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
  padding: 4rem 2rem;
}

.not-found h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: #333;
}

.not-found p {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 2rem;
}

.btn {
  display: inline-block;
  padding: 0.8rem 1.5rem;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.btn:hover {
  background-color: #0056b3;
}
</style> 