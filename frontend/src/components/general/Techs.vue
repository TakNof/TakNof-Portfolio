<template>
  <section id="tech-stack" class="section">
    <div class="section-title">
      <h2>Tech Stack</h2>
      <div class="title-line"></div>
    </div>

    <TechBranches
      :branches="branches"
      :activeBranch="activeBranch"
      @update-branch="$emit('update-branch', $event)"
    />

    <div class="techs-grid" :class="{ 'fade-out-in': animate }">
      <TechCard v-for="tech in techs" :key="tech.id || tech.name" :tech="tech" />
    </div>

    <p v-if="!animate && (!techs || techs.length === 0)" class="techs-empty">
      No techs registered for this branch yet.
    </p>
  </section>
</template>

<script setup>
import { ref, watch, inject } from 'vue'

import TechBranches from '@/components/specific/TechBranches.vue'
import TechCard from '@/components/specific/TechCard.vue'

const props = defineProps({
  techs: { type: Array, default: () => [] },
  branches: { type: Array, default: () => [] },
  activeBranch: { type: String, default: '' }
})

defineEmits(['update-branch'])

const api = inject('api')

// Same fade-out / fade-in choreography as the Projects grid.
const animate = ref(false)

watch(() => props.activeBranch, () => {
  animate.value = true
})

watch(() => api.isLoading.value, (loading) => {
  animate.value = !!loading
})
</script>

<style lang="scss" scoped>
.techs-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1.5rem;
  transition: opacity 0.25s ease-out, transform 0.25s ease-out;

  &.fade-out-in {
    opacity: 0;
    transform: translateY(10px);
  }

  @include mobile {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 1rem;
  }
}

.techs-empty {
  text-align: center;
  color: $text-muted;
  margin-top: 2rem;
}
</style>
