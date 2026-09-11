<template>
  <div 
    class="project-card"
    @mouseenter="isHovered = true"
    @mouseleave="isHovered = false"
  >
    <div class="image-wrapper" v-if="project.image || project.video">
      <img 
        v-show="!isHovered || !project.video" 
        :src="project.image" 
        :alt="project.title" 
      />
      <video 
        v-if="isHovered && project.video"
        :src="project.video"
        class="hover-video"
        muted
        autoplay
        loop
        playsinline
      ></video>
      <div class="category-badge">{{ typeof project.category === 'object' && project.category !== null ? project.category.name : project.category }}</div>
    </div>
    
    <div class="card-content">
      <h3>{{ project.title }}</h3>
      
      <div class="skills_stack">
        <span v-for="skill in (project.skills || [])" :key="skill.id || skill.name" class="tech-badge">
          {{ skill.name }}
        </span>
      </div>

      <div class="techs_stack" v-if="project.techs && project.techs.length">
        <span v-for="tech in project.techs" :key="tech.id || tech.name" class="tech-chip">
          {{ tech.name }}
        </span>
      </div>

      <p class="short-desc">{{ project.shortDesc }}</p>
      
      <router-link :to="`/project/${project.id}`" class="details-btn">
        View Details
        <span class="arrow">→</span>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// Receive the single 'project' object passed from Projects.vue
defineProps({
  project: {
    type: Object,
    required: true
  }
})

const isHovered = ref(false)
</script>

<style lang="scss" scoped>
/* NOTE: Make sure your SCSS variables ($bg-card, $border-color, etc.) 
   are imported or globally available for this to compile! */

.project-card {
  @include glass-panel($bg-card, $border-color, 12px);
  border-radius: $border-radius-lg;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  height: 100%;
  transition: $transition-normal;
  
  &:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6), 0 0 20px rgba($color-dev, 0.15);
    border-color: rgba($color-dev, 0.3);
    
    /* This will still scale the image if there is NO video */
    .image-wrapper img {
      transform: scale(1.05);
    }
    
    .details-btn {
      background: linear-gradient(135deg, $color-dev, $color-art);
      border-color: transparent;
      color: white;
      box-shadow: 0 4px 15px rgba($color-dev, 0.3);
      
      .arrow {
        transform: translateX(4px);
      }
    }
  }
}

.image-wrapper {
  position: relative;
  width: 100%;
  height: 200px;
  overflow: hidden;
  border-bottom: 1px solid $border-color;
  
  img, .hover-video {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  img {
    transition: $transition-slow;
  }
}

.category-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: rgba($bg-main, 0.85);
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: $color-art;
  font-family: $font-heading;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.3rem 0.8rem;
  border-radius: $border-radius-full;
  z-index: 2; /* Ensure badge stays above the video */
}

.card-content {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  text-align: left;
  
  h3 {
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: $text-primary;
    line-height: 1.3;
  }
}

.skills_stack {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 1.25rem;
}

.tech-badge {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.06);
  color: $text-secondary;
  font-size: 0.7rem;
  font-family: $font-mono;
  padding: 0.25rem 0.55rem;
  border-radius: $border-radius-sm;
}

.techs_stack {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 1.25rem;
}

.tech-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  background: rgba($color-dev, 0.08);
  border: 1px solid rgba($color-dev, 0.22);
  color: $color-dev;
  font-size: 0.7rem;
  font-family: $font-mono;
  font-weight: 600;
  padding: 0.25rem 0.55rem;
  border-radius: $border-radius-sm;
  transition: $transition-fast;

  &::before {
    content: '';
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: $color-dev;
  }
}

.project-card:hover .tech-chip {
  border-color: rgba($color-dev, 0.4);
}

.short-desc {
  font-size: 0.95rem;
  line-height: 1.5;
  color: $text-secondary;
  margin-bottom: 1.5rem;
  flex-grow: 1;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.details-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 0.75rem;
  font-family: $font-heading;
  font-size: 0.9rem;
  font-weight: 600;
  border-radius: $border-radius-md;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(255, 255, 255, 0.02);
  color: $text-primary;
  cursor: pointer;
  transition: $transition-normal;
  gap: 0.35rem;
  
  .arrow {
    transition: transform 0.2s ease;
  }
}
</style>