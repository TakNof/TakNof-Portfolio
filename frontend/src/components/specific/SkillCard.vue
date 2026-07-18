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

<style lang="scss" scoped>
.skill-card {
  @include glass-panel($bg-card, $border-color, 12px);
  padding: 2.25rem 2rem;
  border-radius: $border-radius-md;
  text-align: left;
  transition: $transition-normal;
  
  &:hover {
    transform: translateY(-5px);
    border-color: rgba($color-dev, 0.25);
    box-shadow: 0 15px 30px rgba(0,0,0,0.5), 0 0 15px rgba($color-dev, 0.15);
    
    .skill-icon {
      background: rgba($color-dev, 0.1);
      border-color: rgba($color-dev, 0.3);
      transform: scale(1.05);
    }
  }
}

.skill-icon {
  width: 55px;
  height: 55px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 14px;
  font-size: 1.8rem;
  @include flex-center;
  margin-bottom: 1.5rem;
  transition: $transition-normal;
}

h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: $text-primary;
  margin-bottom: 0.75rem;
}

p {
  font-size: 0.95rem;
  line-height: 1.6;
  color: $text-secondary;
}
</style>