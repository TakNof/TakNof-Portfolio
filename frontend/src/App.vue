<template>
  <router-view />
</template>

<script setup>
  import { provide } from 'vue'

  import api from './utils/api.js'
  import { ENDPOINTS } from './utils/endpoints.js'

  provide('api', api)
  provide('endpoints', ENDPOINTS)
</script>