<template>
  <footer class="portfolio-footer">
    <div class="footer-content">
      © {{ currentYear }} Alejandro Fonseca Téllez — Personal Portfolio
    </div>
  </footer>
</template>

<script setup>
// Calculate the year once when the component mounts
const currentYear = new Date().getFullYear()
</script>

<style lang="scss" scoped>
.portfolio-footer {
  border-top: 1px solid $border-color;
  padding: 2rem 0;
  margin-top: 6rem;
  text-align: center;
  font-family: $font-heading;
  font-size: 0.85rem;
  color: $text-muted;
  background: rgba(10, 11, 14, 0.4);
  backdrop-filter: blur(8px);
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
  letter-spacing: 0.05em;
}
</style>