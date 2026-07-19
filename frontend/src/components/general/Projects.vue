<template>
  <section id="projects" class="section">
    <div class="section-title animate-on-scroll">
      <h2>Featured Projects</h2>
      <div class="title-line"></div>
    </div>
    
    <ProjectCategories 
      :categories="categories" 
      :activeCategory="activeCategory" 
      @update-category="$emit('update-category', $event)" 
    />
    
    <div class="projects-showcase">
      <h3 class="category-title">{{ activeCategory }}</h3>
      
      <div class="projects-grid" :class="{ 'fade-out-in': animate }">
        <ProjectCard 
          v-for="(project, i) in projects" 
          :key="project.id || i" 
          :project="project" 
        />
      </div>
    </div>
  </section>
</template>

<script setup>
// ref (for state), computed (for derived data), watch (for side effects like useEffect)
import { ref, computed, watch, inject } from 'vue'

import ProjectCategories from '@/components/specific/ProjectCategories.vue'
import ProjectCard from '@/components/specific/ProjectCard.vue'

// 1. Define the props coming from Home.vue
const props = defineProps({
  projects: [Object, Array],
  categories: Array,
  activeCategory: String
})

// 2. Define the events this component will emit up to Home.vue
defineEmits(['update-category'])

// 3. Inject api for global isLoading state
const api = inject('api')

// 4. State for the animation
const animate = ref(false)

// 5. Watchers: Trigger card animations
// - Start exit animation immediately when category tab changes
watch(() => props.activeCategory, () => {
  animate.value = true
})

// - Fade back in immediately when database request completes
watch(() => api.isLoading.value, (loading) => {
  if (loading) {
    animate.value = true
  } else {
    animate.value = false
  }
})
</script>

<style lang="scss" scoped>
.projects-showcase {
  margin-top: 3rem;
}

.category-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: $text-secondary;
  margin-bottom: 2rem;
  text-align: left;
  border-left: 3px solid $color-dev;
  padding-left: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 2.5rem;
  transition: opacity 0.25s ease-out, transform 0.25s ease-out;
  
  &.fade-out-in {
    opacity: 0;
    transform: translateY(10px);
  }

  @include mobile {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}
</style>