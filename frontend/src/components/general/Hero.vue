<template>
  <section id="home" class="hero">
    <div class="floating-elements">
      <div class="floating-element"></div>
      <div class="floating-element"></div>
      <div class="floating-element"></div>
    </div>

    <div class="hero-inner">
      <div class="hero-content">
        <h1>Alejandro Fonseca Téllez</h1>
        <p class="subtitle">Multimedia Engineer</p>

        <p class="description">
          Perfectionist. Calculated. Architecture-focused. I engineer games,
          web, and immersive experiences down to the last detail.
        </p>

        <ul class="hero-traits">
          <li>Perfectionist</li>
          <li>Calculated</li>
          <li>Architecture-focused</li>
          <li>Detail-obsessed</li>
        </ul>

        <router-link to="/#projects" class="cta-button fade-in-up">
          See projects
        </router-link>
      </div>

      <div class="hero-carousel">
        <ProjectCarousel :projects="projects" />
      </div>
    </div>
  </section>
</template>

<script setup>
import ProjectCarousel from '@/components/specific/ProjectCarousel.vue'

defineProps({
  // Featured projects for the carousel, already selected and ordered by the Home view.
  projects: { type: Array, default: () => [] }
})
</script>

<style lang="scss" scoped>
@use "sass:color";

.hero {
  position: relative;
  overflow: hidden;
  min-height: 50vh;
  display: flex;
  align-items: center;
  // padding: 6rem 0;

  @include tablet {
    min-height: auto;
    padding: 4rem 0;
  }
}

.floating-elements {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
}

.floating-element {
  position: absolute;
  border-radius: 50%;
  mix-blend-mode: screen;
  animation: float 20s infinite ease-in-out;

  &:nth-child(1) {
    width: 350px;
    height: 350px;
    background: rgba($color-dev, 0.15);
    filter: blur(80px);
    top: 10%;
    left: 10%;
    animation-delay: 0s;
  }

  &:nth-child(2) {
    width: 400px;
    height: 400px;
    background: rgba($color-art, 0.12);
    filter: blur(90px);
    bottom: 10%;
    right: 5%;
    animation-delay: -5s;
    animation-duration: 25s;
  }

  &:nth-child(3) {
    width: 250px;
    height: 250px;
    background: rgba($color-creativity, 0.08);
    filter: blur(70px);
    top: 40%;
    left: 45%;
    animation-delay: -10s;
    animation-duration: 18s;
  }
}

@keyframes float {
  0%, 100% {
    transform: translateY(0) scale(1) rotate(0deg);
  }
  33% {
    transform: translateY(-30px) scale(1.1) rotate(120deg);
  }
  66% {
    transform: translateY(20px) scale(0.9) rotate(240deg);
  }
}

.hero-inner {
  position: relative;
  z-index: 2;
  width: 100%;
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 4rem;
  align-items: center;
  margin: 20vh 0;

  @include desktop {
    gap: 2.5rem;
  }

  @include tablet {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
}

.hero-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;

  h1 {
    font-size: 3.75rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #ffffff 20%, #b2bac2 80%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;

    @include desktop {
      font-size: 3rem;
    }

    @include tablet {
      font-size: 2.5rem;
    }
  }

  .subtitle {
    font-family: $font-heading;
    font-size: 1.35rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 1.75rem;
    background: linear-gradient(90deg, $color-dev, $color-art);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;

    @include tablet {
      font-size: 1.1rem;
      margin-bottom: 1.25rem;
    }
  }

  .description {
    font-size: 1.15rem;
    color: $text-secondary;
    line-height: 1.6;
    margin-bottom: 1.5rem;
    max-width: 34ch;

    @include tablet {
      font-size: 1.02rem;
    }
  }
}

.hero-traits {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 2.5rem;

  li {
    font-family: $font-mono;
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: $color-dev;
    border: 1px solid rgba($color-dev, 0.3);
    background: rgba($color-dev, 0.06);
    padding: 0.3rem 0.7rem;
    border-radius: $border-radius-full;
  }
}

.hero-carousel {
  width: 100%;

  @include tablet {
    max-width: 520px;
    margin: 0 auto;
  }
}

.cta-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 1rem 2.2rem;
  font-family: $font-heading;
  font-size: 1.05rem;
  font-weight: 600;
  border-radius: $border-radius-md;
  background: linear-gradient(135deg, $color-dev 0%, color.adjust($color-dev, $lightness: -10%) 100%);
  color: white;
  box-shadow: 0 4px 20px rgba($color-dev, 0.25), 0 0 0 1px rgba(255, 255, 255, 0.05) inset;
  transition: $transition-normal;
  border: none;
  cursor: pointer;

  &:hover {
    background: linear-gradient(135deg, color.adjust($color-dev, $lightness: 5%) 0%, $color-dev 100%);
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba($color-dev, 0.4), 0 0 15px rgba($color-art, 0.3);
  }

  &:active {
    transform: translateY(-1px);
  }
}
</style>
