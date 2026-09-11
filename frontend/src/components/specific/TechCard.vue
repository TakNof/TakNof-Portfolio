<template>
  <div class="tech-card">
    <div class="tech-logo">
      <img
        v-if="!logoFailed"
        :src="logoUrl"
        :alt="`${tech.name} logo`"
        loading="lazy"
        @error="logoFailed = true"
      />
      <span v-else class="tech-logo-fallback">{{ initials }}</span>
    </div>

    <h4 class="tech-name">{{ tech.name }}</h4>

    <div
      class="tech-rate"
      :style="{ '--rate-t': rateFraction }"
      :title="`${rateValue} / 10`"
      :aria-label="`Proficiency ${rateValue} out of 10`"
    >
      <span class="rate-bound">0</span>
      <div class="rate-track">
        <div class="rate-fill" :style="{ width: fillPct + '%' }"></div>
        <div class="rate-ticks" aria-hidden="true"></div>
      </div>
      <span class="rate-bound">10</span>
    </div>

    <!-- Overlay that expands downwards on hover -->
    <div class="tech-projects" v-if="hasProjects">
      <p class="tech-projects-label">Used in</p>
      <ul>
        <li v-for="project in tech.projects" :key="project.id">
          <router-link :to="`/project/${project.id}`">
            <span class="dot"></span>{{ project.title }}
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  tech: { type: Object, required: true }
})

const logoFailed = ref(false)

// "C#" -> "csharp", "Fl Studio" -> "fl-studio", "Vue2 / 3" -> "vue2-3"
const slug = computed(() =>
  props.tech.name
    .trim()
    .toLowerCase()
    .replace(/\+/g, 'plus')
    .replace(/#/g, 'sharp')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '')
)

const logoUrl = computed(() => `/img/techs/${slug.value}.png`)

const initials = computed(() =>
  props.tech.name
    .replace(/[^a-zA-Z0-9]+/g, ' ')
    .trim()
    .split(' ')
    .slice(0, 2)
    .map((w) => w[0])
    .join('')
    .toUpperCase()
)

const rateValue = computed(() => {
  const r = Number(props.tech.rate)
  return Number.isFinite(r) ? Math.min(10, Math.max(0, r)) : 0
})

const fillPct = computed(() => rateValue.value * 10)

// 0 -> 1, drives the bar's colour intensity and glow via a CSS custom property.
const rateFraction = computed(() => rateValue.value / 10)

const hasProjects = computed(
  () => Array.isArray(props.tech.projects) && props.tech.projects.length > 0
)
</script>

<style lang="scss" scoped>
.tech-card {
  position: relative;
  z-index: 1;
  @include glass-panel($bg-card, $border-color, 12px);
  padding: 1.75rem 1.25rem 1.5rem;
  border-radius: $border-radius-md;
  text-align: center;
  transition: $transition-normal;

  &:hover {
    transform: translateY(-4px);
    border-color: rgba($color-dev, 0.3);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5), 0 0 15px rgba($color-dev, 0.15);
    z-index: 20; // sit above sibling cards while the overlay is open
  }
}

.tech-logo {
  width: 60px;
  height: 60px;
  margin: 0 auto 1rem;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.06);
  @include flex-center;
  overflow: hidden;
  transition: $transition-normal;

  img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    padding: 8px;
  }
}

.tech-logo-fallback {
  font-family: $font-heading;
  font-weight: 700;
  font-size: 1.4rem;
  color: $color-dev;
}

.tech-card:hover .tech-logo {
  background: rgba($color-dev, 0.1);
  border-color: rgba($color-dev, 0.3);
  transform: scale(1.05);
}

.tech-name {
  font-family: $font-heading;
  font-size: 1rem;
  font-weight: 700;
  color: $text-primary;
  margin-bottom: 1rem;
}

.tech-rate {
  display: flex;
  align-items: center;
  gap: 0.5rem;

  .rate-bound {
    font-family: $font-mono;
    font-size: 0.75rem;
    color: $text-muted;
  }
}

.rate-track {
  position: relative;
  flex: 1;
  height: 10px;
  border-radius: $border-radius-full;
  background: rgba(255, 255, 255, 0.06);
  /* no overflow:hidden — the fill's glow needs to bleed past the track */
}

.rate-fill {
  position: relative;
  height: 100%;
  border-radius: $border-radius-full;
  background: linear-gradient(90deg, $color-dev, $color-art);
  /* brighter + more saturated the higher the rate */
  filter:
    brightness(calc(0.78 + 0.5 * var(--rate-t, 0)))
    saturate(calc(0.6 + 0.9 * var(--rate-t, 0)));
  /* glow grows in spread and strength with the rate */
  box-shadow:
    0 0 calc(3px + 20px * var(--rate-t, 0)) rgba($color-dev, calc(0.1 + 0.6 * var(--rate-t, 0))),
    0 0 calc(1px + 8px * var(--rate-t, 0)) rgba($color-art, calc(0.08 + 0.5 * var(--rate-t, 0)));
  transition:
    width 0.5s cubic-bezier(0.16, 1, 0.3, 1),
    filter 0.4s ease,
    box-shadow 0.4s ease;
}

/* 10 unit divisions (lines at every 10%) laid over the whole track */
.rate-ticks {
  position: absolute;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  border-radius: inherit;
  background: repeating-linear-gradient(
    to right,
    transparent 0,
    transparent calc(10% - 1px),
    rgba(255, 255, 255, 0.4) calc(10% - 1px),
    rgba(255, 255, 255, 0.4) 10%
  );
}

/* Hover-expand overlay */
.tech-projects {
  position: absolute;
  top: calc(100% - 4px); // overlap the card edge so the hover target has no gap
  left: 0;
  right: 0;
  z-index: 20;
  max-height: 0;
  opacity: 0;
  overflow: hidden;
  text-align: left;
  background: $bg-card-hover;
  backdrop-filter: blur(16px);
  border: 1px solid $border-color;
  border-top: none;
  border-radius: 0 0 $border-radius-md $border-radius-md;
  transition: max-height 0.3s ease, opacity 0.2s ease, padding 0.3s ease;
  pointer-events: none;
}

.tech-card:hover .tech-projects {
  max-height: 260px;
  opacity: 1;
  padding: 1rem 1.25rem 1.25rem;
  overflow-y: auto;
  pointer-events: auto;
  box-shadow: $shadow-lg;
}

.tech-projects-label {
  font-family: $font-heading;
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: $text-muted;
  margin-bottom: 0.5rem;
}

.tech-projects ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}

.tech-projects a {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.4rem 0.5rem;
  border-radius: $border-radius-sm;
  font-size: 0.85rem;
  color: $text-secondary;
  transition: $transition-fast;

  .dot {
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: $color-dev;
    flex-shrink: 0;
  }

  &:hover {
    background: rgba($color-dev, 0.1);
    color: $text-primary;
  }
}
</style>
