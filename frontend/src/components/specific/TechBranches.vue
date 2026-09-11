<template>
  <nav class="tech-branches-nav">
    <div class="tech-branches-grid">
      <button
        v-for="branch in branches"
        :key="branch.name + ' ' + branch.id"
        @click="$emit('update-branch', branch.name)"
        class="branch-button"
        :class="{ 'active-branch': branch.name === activeBranch }"
      >
        {{ branch.name }}
      </button>
    </div>
  </nav>
</template>

<script setup>
defineProps({
  branches: {
    type: Array,
    required: true
  },
  activeBranch: {
    type: String,
    required: true
  }
})

defineEmits(['update-branch'])
</script>

<style lang="scss" scoped>
.tech-branches-nav {
  display: flex;
  justify-content: center;
  margin-bottom: 3rem;
}

.tech-branches-grid {
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

.branch-button {
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

  &.active-branch {
    background: linear-gradient(135deg, $color-dev, $color-art);
    color: $bg-main;          // dark text — legible on the bright green/teal fill
    font-weight: 700;
    box-shadow: 0 4px 15px rgba($color-dev, 0.3);
  }
}
</style>
