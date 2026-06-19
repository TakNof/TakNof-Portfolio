<template>
  <nav class="project-categories-nav">
    <div class="project-categories-grid">
      <!-- 
        v-for replaces categories.map()
        @click emits the custom event to the parent (Projects.vue) 
      -->
      <button
        v-for="(cat, i) in categories"
        :key="cat + ' ' + i"
        @click="$emit('update-category', cat)"
        class="category-button"
        :class="{ 'active-category': cat === activeCategory }"
      >
        {{ cat }}
      </button>
    </div>
  </nav>
</template>

<script setup>
// 1. Define the props we receive from Projects.vue
// Note: We DO NOT receive setActiveCategory as a prop here!
defineProps({
  categories: {
    type: Array,
    required: true
  },
  activeCategory: {
    type: String,
    required: true
  }
})

// 2. Declare the events this component can emit
defineEmits(['update-category'])
</script>

<style scoped>
/* Scoped styles for your categories navigation go here */
</style>