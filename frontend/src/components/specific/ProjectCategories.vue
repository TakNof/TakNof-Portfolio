<template>
  <nav class="project-categories-nav">
    <div class="project-categories-grid">
      <!-- 
        v-for replaces categories.map()
        @click emits the custom event to the parent (Projects.vue) 
      -->
      <button
        v-for="category in categories"
        :key="category.name + ' ' + category.id"
        @click="$emit('update-category', category.name)"
        class="category-button"
        :class="{ 'active-category': category.name === activeCategory }"
      >
        {{ category.name }}
      </button>
    </div>
  </nav>
</template>

<script setup>
import { onMounted } from 'vue';

// 1. Define the props we receive from Projects.vue
// Note: We DO NOT receive setActiveCategory as a prop here!
const props = defineProps({
  categories: {
    type: Array,
    required: true
  },
  activeCategory: {
    type: String,
    required: true
  }
})

onMounted(() => {
  console.log(props.categories);
})

defineEmits(['update-category'])
</script>

<style lang="scss" scoped>
.project-categories-nav {
  display: flex;
  justify-content: center;
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
  border: 1px solid transparent;
  background: transparent;
  color: $text-primary;
  cursor: pointer;
  transition: $transition-normal;

  &:hover {
    color: $text-primary;
    background: rgba(255, 255, 255, 0.06);
    border-color: rgba(255, 255, 255, 0.08);
  }

  &.active-category {
    background: linear-gradient(135deg, $color-dev, $color-art);
    color: $bg-main;          // dark text — legible on the bright green/teal fill
    font-weight: 700;
    box-shadow: 0 4px 15px rgba($color-dev, 0.3);
  }
}
</style>