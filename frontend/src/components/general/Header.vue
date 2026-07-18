<template>
  <header>
    <nav class="main-nav">
      <div class="logo">Alejandro Fonseca Téllez</div>
      <ul class="nav-links">
        <!-- 
          className becomes class.
          Link becomes router-link.
          I changed /home to / to match the router setup we did earlier!
        -->
        <li><router-link to="">Home</router-link></li>
        <li><router-link to="/#projects">Projects</router-link></li>
        <li><router-link to="/#about-me">About me</router-link></li>
        <li><router-link to="/#skills">Skills</router-link></li>
        <li><router-link to="/#contact-me">Contact me</router-link></li>
      </ul>
    </nav>
  </header>
</template>

<script setup>
// router-link is registered globally by Vue Router, 
// so you don't even need to import it here!
</script>

<style lang="scss" scoped>
header {
  position: sticky;
  top: 0;
  z-index: 100;
  width: 100%;
}

.main-nav {
  @include glass-panel($bg-nav, rgba(255, 255, 255, 0.05), 16px);
  border-top: none;
  border-left: none;
  border-right: none;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 3rem;
  transition: $transition-normal;

  @include tablet {
    padding: 0 1.5rem;
  }
}

.logo {
  font-family: $font-heading;
  font-weight: 800;
  font-size: 1.25rem;
  letter-spacing: -0.02em;
  background: linear-gradient(135deg, $color-dev 30%, $color-art 70%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  cursor: default;
  position: relative;
  
  &::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 30%;
    height: 2px;
    background: linear-gradient(90deg, $color-dev, $color-art);
    border-radius: $border-radius-full;
  }
}

.nav-links {
  display: flex;
  gap: 1rem;
  list-style: none;
  align-items: center;

  a {
    font-family: $font-heading;
    font-size: 0.95rem;
    font-weight: 500;
    color: $text-secondary;
    padding: 0.5rem 1rem;
    border-radius: $border-radius-md;
    border: 1px solid transparent;

    &:hover {
      color: $text-primary;
      background: rgba(255, 255, 255, 0.03);
      border-color: rgba(255, 255, 255, 0.05);
    }
  }

  @include tablet {
    display: none; // Minimalist approach: can hide or do simple burger. Let's make it clean and simple, or let it stack for tablets. Actually, let's keep it display flex but with smaller font/gap for tablets, or wrap. Let's see:
  }
}

// For responsive small screens let's shrink navigation
@media (max-width: 768px) {
  .logo {
    font-size: 1.1rem;
  }
  .nav-links {
    display: flex;
    gap: 0.25rem;
    a {
      padding: 0.4rem 0.6rem;
      font-size: 0.85rem;
    }
  }
}

@media (max-width: 480px) {
  .nav-links {
    // Hide details for extremely small screens except projects and contact
    li:nth-child(3), li:nth-child(4) {
      display: none;
    }
  }
}
</style>