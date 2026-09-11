<template>
  <div
    v-if="projects.length"
    class="project-carousel"
    @mouseenter="pause"
    @mouseleave="resume"
  >
    <div class="carousel-viewport">
      <transition :name="transitionName">
        <router-link
          :key="current.id"
          :to="`/project/${current.id}`"
          class="carousel-slide"
        >
          <video
            v-if="current.video"
            :src="current.video"
            :aria-label="current.title"
            class="slide-media"
            autoplay
            loop
            muted
            playsinline
          ></video>
          <img
            v-else-if="current.image"
            :src="current.image"
            :alt="current.title"
            class="slide-media"
            draggable="false"
          />
          <div class="slide-overlay">
            <span class="slide-kicker">{{ current.category?.name || 'Project' }}</span>
            <h3 class="slide-title">{{ current.title }}</h3>
            <p v-if="current.shortDesc" class="slide-desc">{{ current.shortDesc }}</p>
            <span class="slide-cta">View project →</span>
          </div>
        </router-link>
      </transition>

      <div
        v-if="projects.length > 1"
        class="progress-track"
        role="progressbar"
        aria-label="Time until next project"
        aria-valuemin="0"
        aria-valuemax="100"
      >
        <span
          :key="progressKey"
          class="progress-bar"
          :class="{ active: progressActive }"
          :style="{ '--progress-duration': `${props.interval}ms` }"
        ></span>
      </div>

      <button
        v-if="projects.length > 1"
        class="nav prev"
        type="button"
        aria-label="Previous project"
        @click="go(-1)"
      >‹</button>
      <button
        v-if="projects.length > 1"
        class="nav next"
        type="button"
        aria-label="Next project"
        @click="go(1)"
      >›</button>
    </div>

    <div v-if="projects.length > 1" class="carousel-dots">
      <button
        v-for="(project, i) in projects"
        :key="project.id"
        type="button"
        class="dot"
        :class="{ active: i === index }"
        :aria-label="`Go to ${project.title}`"
        @click="goTo(i)"
      ></button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  projects: { type: Array, default: () => [] },
  interval: { type: Number, default: 10000 },
  cooldown: { type: Number, default: 5000 }
})

const index = ref(0)
const transitionName = ref('slide-next')
const current = computed(() => props.projects[index.value] || {})
const progressKey = ref(0)
const progressActive = ref(false)

let timer = null
let cooldownTimer = null
let isHovered = false

const start = () => {
  stop()
  if (cooldownTimer || isHovered) return
  if (props.projects.length > 1) {
    progressActive.value = true
    progressKey.value += 1
    timer = setInterval(() => advance(1), props.interval)
  }
}
const stop = () => {
  if (timer) clearInterval(timer)
  timer = null
  progressActive.value = false
}
const clearCooldown = () => {
  if (cooldownTimer) clearTimeout(cooldownTimer)
  cooldownTimer = null
}
const scheduleResume = () => {
  clearCooldown()
  cooldownTimer = setTimeout(() => {
    cooldownTimer = null
    start()
  }, props.cooldown)
}
const pause = () => {
  isHovered = true
  stop()
}
const resume = () => {
  isHovered = false
  start()
}

const advance = (dir) => {
  const n = props.projects.length
  if (!n) return
  transitionName.value = dir > 0 ? 'slide-next' : 'slide-prev'
  index.value = (index.value + dir + n) % n
  progressKey.value += 1
}
const go = (dir) => {
  stop()
  advance(dir)
  scheduleResume()
}
const goTo = (i) => {
  stop()
  transitionName.value = i >= index.value ? 'slide-next' : 'slide-prev'
  index.value = i
  scheduleResume()
}

onMounted(start)
onUnmounted(() => {
  stop()
  clearCooldown()
})
</script>

<style lang="scss" scoped>
.project-carousel {
  width: 100%;
}

.carousel-viewport {
  position: relative;
  aspect-ratio: 16 / 9;
  border-radius: $border-radius-lg;
  overflow: hidden;
  background: $bg-code;
  @include glass-panel($bg-card, $border-color, 12px);
  box-shadow: $shadow-lg, 0 0 40px rgba($color-dev, 0.15);
}

.carousel-slide {
  position: absolute;
  inset: 0;
  display: block;
}

.progress-track {
  position: absolute;
  right: 0;
  bottom: 0;
  left: 0;
  height: 3px;
  overflow: hidden;
  background: rgba($text-secondary, 0.18);
  z-index: 4;
}

.progress-bar {
  display: block;
  width: 100%;
  height: 100%;
  transform: scaleX(0);
  transform-origin: left;
  background: linear-gradient(90deg, $color-dev, $color-art);
  box-shadow: none;
  opacity: 0.45;
  animation: carousel-progress var(--progress-duration) linear forwards;
  animation-play-state: paused;
  transition: opacity $transition-fast, box-shadow $transition-normal;

  &.active {
    animation-play-state: running;
    opacity: 1;
    box-shadow: $glow-dev, $glow-art;
  }
}

@keyframes carousel-progress {
  to { transform: scaleX(1); }
}

.slide-media {
  width: 100%;
  height: 100%;
  object-fit: cover;
  user-select: none;
}

.slide-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 0.45rem;
  padding: 1.5rem;
  background: linear-gradient(
    to top,
    rgba(0, 0, 0, 0.88) 0%,
    rgba(0, 0, 0, 0.25) 20%,
    transparent 100%
  );
}

.slide-kicker {
  font-family: $font-mono;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: $color-art;
}

.slide-title {
  font-family: $font-heading;
  font-size: 1.35rem;
  font-weight: 700;
  color: #fff;
  line-height: 1.25;
}

.slide-desc {
  font-size: 0.9rem;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.82);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.slide-cta {
  margin-top: 0.15rem;
  font-family: $font-heading;
  font-size: 0.85rem;
  font-weight: 600;
  color: $color-dev;
}

.nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  border: 1px solid rgba(255, 255, 255, 0.2);
  background: rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(4px);
  color: #fff;
  font-size: 1.5rem;
  line-height: 1;
  cursor: pointer;
  z-index: 3;
  transition: $transition-fast;

  &:hover {
    background: rgba($color-dev, 0.85);
    border-color: transparent;
  }

  &.prev { left: 0.75rem; }
  &.next { right: 0.75rem; }
}

.carousel-dots {
  display: flex;
  justify-content: center;
  gap: 0.4rem;
  margin-top: 1rem;

  .dot {
    width: 8px;
    height: 8px;
    padding: 0;
    border: none;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.22);
    cursor: pointer;
    transition: $transition-fast;

    &.active {
      width: 22px;
      border-radius: $border-radius-full;
      background: linear-gradient(90deg, $color-dev, $color-art);
    }
  }
}

/* cross-fade + directional shift */
.slide-next-enter-active,
.slide-next-leave-active,
.slide-prev-enter-active,
.slide-prev-leave-active {
  transition: opacity 0.45s ease, transform 0.45s ease;
}
.slide-next-enter-from { opacity: 0; transform: translateX(24px); }
.slide-next-leave-to   { opacity: 0; transform: translateX(-24px); }
.slide-prev-enter-from  { opacity: 0; transform: translateX(-24px); }
.slide-prev-leave-to    { opacity: 0; transform: translateX(24px); }
</style>
