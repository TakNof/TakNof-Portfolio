<template>
  <section id="projects" class="section">
    <h2>Projects</h2>
    
    <!-- 
      We pass down the categories and activeCategory.
      When ProjectCategories emits an update, we capture it and re-emit it 
      up to Home.vue using Vue's built-in $emit function.
    -->
    <ProjectCategories 
      :categories="categories" 
      :activeCategory="activeCategory" 
      @update-category="$emit('update-category', $event)" 
    />
    
    <div class="projects-showcase">
      <h2>{{ activeCategory }}</h2>
      
      <!-- Dynamic class binding: 'fade-in-up' is applied only if animate is true -->
      <div class="projects-grid" :class="{ 'fade-in-up': animate }">
        
        <!-- 
          v-bind="project" works EXACTLY like {...project} in React.
          It spreads all the keys of the object as individual props! 
        -->
        <ProjectCard 
          v-for="(project, i) in filteredProjects" 
          :key="project.id || i" 
          v-bind="project" 
        />
        
      </div>
    </div>
  </section>
</template>

<script setup>
// ref (for state), computed (for derived data), watch (for side effects like useEffect)
import { ref, computed, watch } from 'vue'

import ProjectCategories from '@/components/specific/ProjectCategories.vue'
import ProjectCard from '@/components/specific/ProjectCard.vue'

// 1. Define the props coming from Home.vue
const props = defineProps({
  projects: Object,
  categories: Array,
  activeCategory: String
})

// 2. Define the events this component will emit up to Home.vue
defineEmits(['update-category'])

// 3. State for the animation
const animate = ref(false)

// 4. Computed Property: This replaces React's standard variable assignment.
// In Vue, `computed` automatically recalculates whenever `props.activeCategory` changes.
const filteredProjects = computed(() => {
  if (!props.projects || !props.projects.projects) return []
  return props.projects.projects.filter(
    (proj) => proj.category === props.activeCategory
  )
})

// 5. Watcher: This is the equivalent of your useEffect with [activeCategory] dependency!
let timer = null // To hold the timeout reference

watch(() => props.activeCategory, () => {
  animate.value = true
  
  // Clear the previous timer in case the user clicks buttons really fast
  if (timer) clearTimeout(timer)
  
  timer = setTimeout(() => {
    animate.value = false
  }, 500)
})
</script>