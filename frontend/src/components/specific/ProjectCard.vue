<template>
  <div class="project-card">
    <!-- Using Vue data binding (:) for src and alt -->
    <img :src="project.image" :alt="project.title" v-if="project.image" />
    
    <div class="card-content">
      <h3>{{ project.title }}</h3>
      <p class="category">{{ project.category }}</p>
      
      <div class="tech-stack">
        <span v-for="(tech, index) in project.tech" :key="index" class="tech-badge">
          {{ tech }}
        </span>
      </div>

      <p>{{ project.shortDesc }}</p>
      
      <!-- Link to the detail page using the project ID -->
      <router-link :to="`/project/${project.id}`" class="details-btn">
        View Details
      </router-link>
    </div>
  </div>
</template>

<script setup>
// Receive the single 'project' object passed from Projects.vue
defineProps({
  project: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
/* Scoped means this CSS only affects this specific component */
.tech-badge {
  background-color: #333;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  margin-right: 5px;
  font-size: 12px;
}
</style>