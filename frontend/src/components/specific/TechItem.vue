<template>
  <div class="tech-list">
    <!-- Loop through the array of technologies -->
    <span 
      v-for="(item, index) in tech" 
      :key="index" 
      class="tech-badge"
    >
      {{ item }}
    </span>
  </div>
</template>

<script setup>
// Define the props to accept the array of technologies
defineProps({
  tech: {
    type: Array,
    required: true,
    default: () => [] // Fallback to empty array just in case
  }
})
</script>

<style scoped>
/* Container for the badges */
.tech-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px; /* Space between the badges */
  margin-top: 10px;
  margin-bottom: 10px;
}

/* Individual badge styling */
.tech-badge {
  background-color: #25252d; /* Dark modern background */
  color: #e0e0e0;            /* Light gray text */
  padding: 6px 14px;         /* Inner spacing */
  border-radius: 20px;       /* Pill shape */
  font-size: 0.85rem;        /* Slightly smaller text */
  font-weight: 500;
  letter-spacing: 0.5px;
  border: 1px solid #3e3e4a; /* Subtle border */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease; /* Smooth hover transition */
  cursor: default;           /* Standard cursor since they aren't clickable links */
}

/* Hover effect to make it feel interactive/polished */
.tech-badge:hover {
  background-color: #383844;
  border-color: #5a5a6e;
  transform: translateY(-2px); /* Slight lift effect */
}
</style>