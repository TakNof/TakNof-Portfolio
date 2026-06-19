<template>
  <footer class="bg-black py-6 mt-12 text-center text-gray-500 text-sm">
    © {{ currentYear }} Alejandro Fonseca Téllez — Personal Portfolio
  </footer>
</template>

<script setup>
// Calculate the year once when the component mounts
const currentYear = new Date().getFullYear()
</script>

<style scoped>

</style>