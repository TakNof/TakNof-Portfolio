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
    icon: "🔬",
    title: "Attention to Detail",
    desc: "Obsessive polish: I keep refining until every interaction, frame, and edge case feels right."
  },
  {
    icon: "📐",
    title: "Software Architecture",
    desc: "Planning modular, maintainable structures with clear separation of concerns before the first line of code."
  },
  {
    icon: "♟️",
    title: "Calculated Decisions",
    desc: "Weighing trade-offs deliberately and measuring before committing to an approach."
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
  },
  {
    icon: "🧱",
    title: "End-to-End Ownership",
    desc: "Carrying a project from data model and backend through to a polished, deployed interface."
  },
  {
    icon: "🎛️",
    title: "Cross-disciplinary Craft",
    desc: "Bridging engineering with 3D, audio, and design to ship complete, cohesive experiences."
  },
  {
    icon: "🤝",
    title: "Team Leadership",
    desc: "Coordinating small development teams, scoping work, and keeping delivery on track."
  },
  {
    icon: "⚡",
    title: "Fast Learning",
    desc: "Quickly adapting to new technologies, tools, and programming languages."
  }
]
</script>

<style lang="scss" scoped>
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 2rem;
  
  @include tablet {
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.5rem;
  }
  
  @include mobile {
    grid-template-columns: 1fr;
  }
}
</style>