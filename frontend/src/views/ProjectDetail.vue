<template>
  <Header />

  <!-- If project is not found -->
  <div v-if="!projectInfo">
    <h2>Proyecto no encontrado</h2>
  </div>

  <!-- If project IS found -->
  <div v-else class="project-detail">
    <button class="return-btn" @click="goBack">
      Return
    </button>

    <div>
      <h2>{{ projectInfo.title }}</h2>
      
      <div class="project-image">
        <!-- v-if handles the check for undefined or empty strings -->
        <video
          v-if="projectInfo.video"
          ref="videoRef"
          :src="projectInfo.video"
          muted
          autoplay
          loop
          class="project-preview"
        ></video>
      </div>

      <h4 class="project-date">{{ projectInfo.date }}</h4>
      <h4 class="project-status">Status: {{ projectInfo.status }}</h4>
      
      <div class="project-tech">
        <!-- Passing the tech array as a prop to TechItem -->
        <TechItem :tech="projectInfo.tech" />
      </div>
    </div>

    <div class="detail-title">
      <h1>Project Information</h1>
      <nav class="detail-nav">
        <!-- Updating state directly in the @click handler -->
        <button class="category-button" @click="tab = 'General'">General</button>
        <button class="category-button" @click="tab = 'Detailed'">Detailed</button>
      </nav>
    </div>

    <!-- TABS RENDERING -->
    <section v-if="tab === 'General'" class="general-description">
      <p>{{ projectInfo.info.generalInfo.desc }}</p>
      
      <img 
        v-if="projectInfo.info.generalInfo.image" 
        :src="projectInfo.info.generalInfo.image" 
        alt="Not found" 
      />
    </section>

    <section v-else class="detailed-description">
      <!-- v-for replaces React's .map() -->
      <div v-for="(feat, i) in projectInfo.info.detailedInfo" :key="i" class="feature">
        <h3>{{ feat.title }}</h3>
        
        <img 
          v-if="feat.image" 
          :src="feat.image" 
          :alt="feat.title" 
        />
        
        <!-- Nested v-for for the paragraphs -->
        <p v-for="(p, j) in feat.paragraphs" :key="j">
          {{ p }}
        </p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import Header from '@/components/general/Header.vue'
import TechItem from '@/components/specific/TechItem.vue' // NOTE: You need to create this as a separate file in Vue!

import projectsData from '@/scripts/projectsData.json'
import '@/ProjectDetail.css' // You can import CSS exactly like React

const route = useRoute()
const router = useRouter()

// 1. Get ID from URL
const projectId = route.params.id

// 2. Find Project
const projectInfo = projectsData.projects.find(p => p.id.toString() === projectId)

// 3. Setup State and Refs
// Note: In your React code, you initialized this as "general" (lowercase), 
// but checked for "General" (uppercase). I fixed it to uppercase here to prevent bugs.
const tab = ref("General") 

// Equivalent to useRef(null)
const videoRef = ref(null)

// 4. Methods
const goBack = () => {
  router.push("/")
}
</script>