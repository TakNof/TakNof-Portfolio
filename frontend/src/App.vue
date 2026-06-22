<template>
  <MainView />
</template>

<script setup>
import { provide } from 'vue'
import MainView from './views/MainView.vue'

import api from '../utils/api'
import { ENDPOINTS } from '../utils/endpoints'

provide('api', api)
provide('endpoints', ENDPOINTS)
</script>