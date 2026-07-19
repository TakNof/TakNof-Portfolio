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
      <h1 class="project-title">{{ projectInfo.title }}</h1>
      
      <div class="project-preview-wrapper">
        <!-- v-if handles the check for undefined or empty strings -->
        <video
          v-if="projectInfo.video"
          ref="videoRef"
          :src="projectInfo.video"
          muted
          autoplay
          loop
        ></video>
        <img
          v-else-if="projectInfo.image"
          :src="projectInfo.image"
          :alt="projectInfo.title"
        />
      </div>

      <div class="project-meta">
        <span class="project-date">{{ projectInfo.date }}</span>
        <span class="project-status">Status: {{ projectInfo.status }}</span>
        <div class="project-tech">
          <!-- Passing the tech array as a prop to TechItem -->
          <TechItem :tech="projectInfo.tech" />
        </div>
      </div>
    </div>

    <div class="detail-title">
      <h1>Project Information</h1>
      <nav class="detail-nav">
        <!-- Updating state directly in the @click handler and binding active class -->
        <button class="category-button" :class="{ 'active-tab': tab === 'General' }" @click="tab = 'General'">General</button>
        <button class="category-button" :class="{ 'active-tab': tab === 'Detailed' }" @click="tab = 'Detailed'">Detailed</button>
      </nav>
    </div>

    <!-- TABS RENDERING -->
    <section v-if="tab === 'General'" class="general-description">
      <p>{{ projectInfo.info?.generalInfo?.desc || projectInfo.shortDesc }}</p>
      
      <img 
        v-if="projectInfo.info?.generalInfo?.image" 
        :src="projectInfo.info.generalInfo.image" 
        alt="Not found" 
      />
    </section>

    <section v-else class="detailed-description">
      <!-- v-for replaces React's .map() -->
      <div v-for="(feat, i) in projectInfo.info?.detailedInfo" :key="i" class="feature">
        <h3 v-if="feat.title">{{ feat.title }}</h3>
        
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
      <div v-if="!projectInfo.info?.detailedInfo || projectInfo.info.detailedInfo.length === 0" class="no-details">
        <p>No detailed information available for this project yet.</p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import Header from '@/components/general/Header.vue'

import projectsData from '@/scripts/projectsData.json'

const route = useRoute()
const router = useRouter()

// 1. Get ID from URL
const projectId = route.params.id

// 2. Find Project
const projectInfo = projectsData.projects.find(p => p.id.toString() === projectId)

// 3. Setup State and Refs
const tab = ref("General") 

// Equivalent to useRef(null)
const videoRef = ref(null)

// 4. Methods
const goBack = () => {
  router.push("/")
}
</script>

<style lang="scss" scoped>
@use "sass:color";

.project-detail {
  max-width: 900px;
  margin: 3rem auto 6rem;
  padding: 0 1.5rem;
  text-align: left;
}

.return-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: $font-heading;
  font-weight: 600;
  font-size: 0.95rem;
  padding: 0.6rem 1.4rem;
  border-radius: $border-radius-md;
  border: 1px solid $border-color;
  background: rgba(255, 255, 255, 0.02);
  color: $text-secondary;
  margin-bottom: 2.5rem;
  cursor: pointer;
  transition: $transition-normal;
  
  &:hover {
    color: $text-primary;
    border-color: rgba(255, 255, 255, 0.15);
    background: rgba(255, 255, 255, 0.05);
    transform: translateX(-4px);
  }
}

.project-title {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 1.5rem;
  letter-spacing: -0.03em;
  background: linear-gradient(135deg, #ffffff 30%, #c0c0c0 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  
  @include tablet {
    font-size: 2rem;
  }
}

.project-preview-wrapper {
  @include glass-panel($bg-card, $border-color, 16px);
  border-radius: $border-radius-lg;
  overflow: hidden;
  margin-bottom: 2.5rem;
  box-shadow: $shadow-lg, 0 0 40px rgba($color-dev, 0.15);
  position: relative;
  aspect-ratio: 16 / 9;
  
  video, img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }
}

.project-meta {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 2rem;
  background: rgba(255, 255, 255, 0.01);
  padding: 1.5rem;
  border-radius: $border-radius-md;
  border: 1px solid rgba(255, 255, 255, 0.04);
}

.project-date {
  font-size: 0.95rem;
  font-weight: 500;
  color: $text-muted;
}

.project-status {
  font-size: 0.95rem;
  font-weight: 600;
  color: $color-art;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.project-tech {
  margin-top: 0.5rem;
}

.detail-title {
  margin-top: 4rem;
  border-top: 1px solid $border-color;
  padding-top: 3rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1.5rem;
  margin-bottom: 2.5rem;
  
  h1 {
    font-size: 1.75rem;
    font-weight: 700;
    margin: 0;
  }
}

.detail-nav {
  display: flex;
  gap: 0.4rem;
  background: rgba(255, 255, 255, 0.02);
  padding: 0.3rem;
  border-radius: $border-radius-md;
  border: 1px solid $border-color;
  backdrop-filter: blur(8px);
}

.category-button {
  font-family: $font-heading;
  font-size: 0.9rem;
  font-weight: 600;
  padding: 0.5rem 1.2rem;
  border-radius: $border-radius-sm;
  border: none;
  background: transparent;
  color: $text-secondary;
  cursor: pointer;
  transition: $transition-normal;
  
  &:hover {
    color: $text-primary;
  }
  
  &.active-tab {
    background: linear-gradient(135deg, $color-dev, color.adjust($color-dev, $lightness: -10%));
    color: white;
    box-shadow: 0 4px 12px rgba($color-dev, 0.25);
  }
}

.general-description, .detailed-description {
  @include glass-panel($bg-card, $border-color, 12px);
  padding: 2.5rem;
  border-radius: $border-radius-lg;
  
  @include tablet {
    padding: 1.5rem;
  }
  
  p {
    font-size: 1.05rem;
    line-height: 1.7;
    color: $text-secondary;
    margin-bottom: 1.5rem;
    
    &:last-of-type {
      margin-bottom: 0;
    }
  }
  
  img {
    width: 100%;
    max-height: 500px;
    object-fit: cover;
    border-radius: $border-radius-md;
    border: 1px solid $border-color;
    margin-top: 2rem;
  }
}

.detailed-description {
  display: flex;
  flex-direction: column;
  gap: 3.5rem;
  
  .feature {
    h3 {
      font-size: 1.35rem;
      font-weight: 700;
      color: $text-primary;
      margin-bottom: 1.25rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      padding-bottom: 0.5rem;
    }
    
    img {
      width: 100%;
      max-height: 400px;
      object-fit: cover;
      border-radius: $border-radius-md;
      border: 1px solid $border-color;
      margin-bottom: 1.5rem;
    }
  }
}

.no-details {
  text-align: center;
  color: $text-muted;
  padding: 2rem 0;
}
</style>