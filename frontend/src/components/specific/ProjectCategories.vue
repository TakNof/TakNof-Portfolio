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

<style lang="scss" scoped>
.project-categories-nav {
  display: flex;
  justify-content: center;
  margin-bottom: 3rem;
}

.project-categories-grid {
  display: flex;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid $border-color;
  padding: 0.4rem;
  border-radius: $border-radius-full;
  flex-wrap: wrap;
  justify-content: center;
  backdrop-filter: blur(8px);
}

.category-button {
  font-family: $font-heading;
  font-size: 0.9rem;
  font-weight: 600;
  padding: 0.6rem 1.4rem;
  border-radius: $border-radius-full;
  border: none;
  background: transparent;
  color: $text-secondary;
  cursor: pointer;
  transition: $transition-normal;
  
  &:hover {
    color: $text-primary;
    background: rgba(255, 255, 255, 0.03);
  }
  
  &.active-category {
    background: linear-gradient(135deg, $color-dev, $color-art);
    color: white;
    box-shadow: 0 4px 15px rgba($color-dev, 0.25);
  }
}
</style>