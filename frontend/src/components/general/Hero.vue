<template>
  <section id="home" class="hero">
    <div class="floating-elements">
      <div class="floating-element"></div>
      <div class="floating-element"></div>
      <div class="floating-element"></div>
    </div>
    <div class="hero-content">
      <h1>Alejandro Fonseca Téllez</h1>
      <p class="subtitle">Multimedia Engineer</p>
      <p class="description">
        Game development, web experiences, and software solutions—crafted with precision, passion, and purpose.
        I specialize in web development, audiovisual production, AR, VR, and video games, bringing ideas to life through innovative and high-quality code.  
      </p>
      
      <!-- Replaced React's Link with Vue's router-link -->
      <router-link to="/#projects" class="cta-button fade-in-up">
        See projects
      </router-link>
    </div>
  </section>
</template>

<script setup>
// Since there is no dynamic state or props in this component, 
// the script section can simply remain empty!
</script>

<style scoped>
/* You can put any styles specific only to the Hero section here */
</style>