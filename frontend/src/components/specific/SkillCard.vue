<template>
  <div class="skill-card">
    <div class="skill-icon">{{ icon }}</div>
    <h3>{{ title }}</h3>
    <p>{{ desc }}</p>
  </div>
</template>

<script setup>
// Define the props that this component expects to receive
defineProps({
  icon: {
    type: String,
    required: true
  },
  title: {
    type: String,
    required: true
  },
  desc: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
/* You can isolate your skill card CSS here */
</style>