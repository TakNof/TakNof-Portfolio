<template>
  <MainView />
</template>

<script setup>
  import { provide } from 'vue'
  import MainView from './views/MainView.vue'

  import api from './utils/api.js'
  import { ENDPOINTS } from './utils/endpoints.js'

  provide('api', api)
  provide('endpoints', ENDPOINTS)
</script>