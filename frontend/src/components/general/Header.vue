<template>
  <header>
    <nav class="main-nav">
      <div class="logo">Alejandro Fonseca Téllez</div>
      <ul class="nav-links">
        <!-- 
          className becomes class.
          Link becomes router-link.
          I changed /home to / to match the router setup we did earlier!
        -->
        <li><router-link to="/#home">Home</router-link></li>
        <li><router-link to="/#projects">Projects</router-link></li>
        <li><router-link to="/#about-me">About me</router-link></li>
        <li><router-link to="/#skills">Skills</router-link></li>
        <li><router-link to="/#contact-me">Contact me</router-link></li>
      </ul>
    </nav>
  </header>
</template>

<script setup>
// router-link is registered globally by Vue Router, 
// so you don't even need to import it here!
</script>

<style scoped>
/* Add any header-specific styles here */
</style>