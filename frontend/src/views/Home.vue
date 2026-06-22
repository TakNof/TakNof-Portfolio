<template>
  <!-- In Vue 3, fragments (multiple root elements) are supported just like React's <> -->
  <!-- <Header />
  <Hero /> -->
  
  <!-- 
    Notice the data binding (:) for variables.
    Instead of passing the setter function, we listen for a custom event (@update-category) 
  -->
  <!-- <Projects
    :projects="projectsData"
    :categories="categories" 
    :activeCategory="activeCategory"
    @update-category="setActiveCategory"
  /> -->
  
  <!-- <About />
  <Skills />
  <Contact />
  <Footer /> -->

</template>

<script setup>
// React's `useState` is replaced by Vue's `ref`
import { onMounted, inject, ref } from 'vue'
import axios from 'axios';

// Import components (Make sure to add the .vue extension!)
import Header from '@/components/general/Header.vue'
import Hero from '@/components/general/Hero.vue'
import Projects from '@/components/general/Projects.vue'
import Skills from '@/components/general/Skills.vue'
import About from '@/components/general/About.vue'
import Contact from '@/components/general/Contact.vue'
import Footer from '@/components/general/Footer.vue'

// Import your JSON (Vite handles JSON imports perfectly)
import projectsData from '@/scripts/projectsData.json'
const api = inject("api");
const endpoints = inject('endpoints');

// 1. Get unique categories
const categories = [...new Set(projectsData.projects.map((p) => p.category))]

// 2. State management (equivalent to useState)
const activeCategory = ref(categories[0])

// 3. The state updater function
const setActiveCategory = (newCategory) => {
  activeCategory.value = newCategory // In Vue, you mutate the .value of a ref
}

onMounted(() =>{
  loadCategories();
})

async function loadCategories(){
  const response = await api.get(`${endpoints.PROJECTS}`)
  if(response.status == 200){
    console.log("These are the categories " + response.data);
  }
}
</script>