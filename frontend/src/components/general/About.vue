<template>
  <section id="about-me" class="section">
    <div class="section-title">
      <h2>About Me</h2>
      <div class="title-line"></div>
    </div>
    
    <div class="about-content">
      <div class="profile-image-container">
        <div class="gradient-ring"></div>
        <div class="profile-inner">
          <span class="avatar-emoji">👨‍💻</span>
        </div>
      </div>
      
      <div class="about-card">
        <div class="about-text">
          <p>
            I am a **Multimedia Engineering student**, a developer driven by creativity and technical precision.
            My work is positioned at the intersection of game development, web development, and software engineering.
            I love turning complex concepts into interactive, highly polished experiences—whether that means scripting
            immersive gameplay mechanics, building fluid websites, or architecting robust backend systems.
          </p>
          <p>
            Beyond lines of code, I value the balance between technology and art. I thrive in collaborative environments,
            constantly exploring emerging technologies to stay at the cutting edge of digital product development.
            Whether it's designing a responsive front-end interface, prototyping VR mechanics, or training neural networks,
            I approach each project with rigorous curiosity and a high standard of quality.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
// This component is purely presentational, so the script setup stays empty!
</script>

<style lang="scss" scoped>
.about-content {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 3.5rem;
  align-items: center;
  margin-top: 2rem;
  
  @include tablet {
    grid-template-columns: 1fr;
    gap: 2.5rem;
    justify-items: center;
  }
}

.profile-image-container {
  position: relative;
  width: 240px;
  height: 240px;
  @include flex-center;
  
  .gradient-ring {
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: linear-gradient(135deg, $color-dev, $color-art, $color-creativity);
    animation: spin 8s linear infinite;
    z-index: 1;
    opacity: 0.85;
    box-shadow: 0 0 30px rgba($color-dev, 0.3);
  }
  
  .profile-inner {
    position: absolute;
    width: calc(100% - 10px);
    height: calc(100% - 10px);
    border-radius: 50%;
    background: #0f1118;
    z-index: 2;
    @include flex-center;
    border: 1px solid rgba(255, 255, 255, 0.05);
    
    .avatar-emoji {
      font-size: 5.5rem;
      user-select: none;
      filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.3));
    }
  }
}

@keyframes spin {
  100% {
    transform: rotate(360deg);
  }
}

.about-card {
  @include glass-panel($bg-card, $border-color, 12px);
  padding: 2.5rem;
  border-radius: $border-radius-lg;
  text-align: left;
  box-shadow: $shadow-md;
  
  @include tablet {
    padding: 1.75rem;
  }
}

.about-text {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  
  p {
    font-size: 1.05rem;
    line-height: 1.7;
    color: $text-secondary;
    
    strong {
      color: $text-primary;
      font-weight: 600;
    }
  }
}
</style>