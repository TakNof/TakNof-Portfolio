<template>
  <section id="skills" class="section">
    <div class="section-title">
      <h2>My Skills</h2>
      <div class="title-line"></div>
    </div>
    
    <div class="skills-grid">
      
      <!-- 
        Looping through the skills array using v-for. 
        v-bind="skill" automatically passes icon, title, and desc as separate props! 
      -->
      <SkillCard 
        v-for="(skill, index) in skills" 
        :key="index" 
        v-bind="skill" 
      />

    </div>
  </section>
</template>

<script setup>
// Import the new child component
import SkillCard from '@/components/specific/SkillCard.vue'

// Since this data is static and never changes, we just use a normal array.
// No need for ref() or reactive(), which makes it faster!
const skills = [
  { 
    icon: "💻", 
    title: "Web Development", 
    desc: "Building responsive and interactive websites using HTML, CSS, JavaScript, and Vue/React." 
  },
  { 
    icon: "🎮", 
    title: "Game Development", 
    desc: "Creating engaging games with Unity, Unreal Engine, and JavaScript frameworks." 
  },
  { 
    icon: "🎬", 
    title: "Animation", 
    desc: "Designing smooth and appealing animations with After Effects, Autodesk Maya, and CSS." 
  },
  { 
    icon: "⚡", 
    title: "Fast Learning", 
    desc: "Quickly adapting to new technologies, tools, and programming languages." 
  },
  { 
    icon: "🧠", 
    title: "High Logic Capacity", 
    desc: "Solving complex problems with strong analytical and logical thinking skills." 
  },
  { 
    icon: "🚀", 
    title: "Optimization", 
    desc: "Improving performance and efficiency in code, games, and applications." 
  }
]
</script>

<style lang="scss" scoped>
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
  
  @include tablet {
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.5rem;
  }
  
  @include mobile {
    grid-template-columns: 1fr;
  }
}
</style>