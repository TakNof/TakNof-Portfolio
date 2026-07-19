<template>
  <section id="home" class="hero">
    <div class="floating-elements">
      <div class="floating-element"></div>
      <div class="floating-element"></div>
      <div class="floating-element"></div>
    </div>
    <div class="hero-content">
      <h1>Alejandro Fonseca Téllez</h1>
      <p class="subtitle">Multimedia Engineer</p>
      <p class="description">
        Game development, web experiences, and software solutions—crafted with precision, passion, and purpose.
        I specialize in web development, audiovisual production, AR, VR, and video games, bringing ideas to life through innovative and high-quality code.  
      </p>
      
      <!-- Replaced React's Link with Vue's router-link -->
      <router-link to="/#projects" class="cta-button fade-in-up">
        See projects
      </router-link>
    </div>
  </section>
</template>

<script setup>
// Since there is no dynamic state or props in this component, 
// the script section can simply remain empty!
</script>

<style lang="scss" scoped>
@use "sass:color";

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 80vh;
  padding: 6rem 1.5rem;
  text-align: center;
  position: relative;
  overflow: hidden;
  
  @include tablet {
    min-height: auto;
    padding: 4rem 1.25rem;
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

.hero-content {
  max-width: 850px;
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;

  h1 {
    font-size: 4.5rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #ffffff 20%, #b2bac2 80%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;

    @include tablet {
      font-size: 3rem;
    }
  }

  .subtitle {
    font-family: $font-heading;
    font-size: 1.5rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 2rem;
    background: linear-gradient(90deg, $color-dev, $color-art);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: inline-block;

    @include tablet {
      font-size: 1.15rem;
      margin-bottom: 1.5rem;
    }
  }

  .description {
    font-size: 1.25rem;
    color: $text-secondary;
    line-height: 1.6;
    margin-bottom: 3rem;
    max-width: 700px;

    @include tablet {
      font-size: 1.05rem;
      margin-bottom: 2rem;
    }
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