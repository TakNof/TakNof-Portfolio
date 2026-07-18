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

<style lang="scss" scoped>
.tech-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 10px;
  margin-bottom: 10px;
}

.tech-badge {
  background-color: rgba(255, 255, 255, 0.03);
  color: $text-secondary;
  padding: 6px 14px;
  border-radius: $border-radius-full;
  font-size: 0.8rem;
  font-family: $font-mono;
  font-weight: 500;
  letter-spacing: 0.5px;
  border: 1px solid $border-color;
  box-shadow: $shadow-sm;
  transition: $transition-normal;
  cursor: default;
  
  &:hover {
    background-color: rgba(255, 255, 255, 0.07);
    border-color: rgba($color-art, 0.4);
    color: $text-primary;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3), 0 0 10px rgba($color-art, 0.2);
  }
}
</style>