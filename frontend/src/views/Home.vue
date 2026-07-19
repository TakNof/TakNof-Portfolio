<template>
  <!-- In Vue 3, fragments (multiple root elements) are supported just like React's <> -->
  <Header/>
  <Hero />
  
  <!-- 
    Notice the data binding (:) for variables.
    Instead of passing the setter function, we listen for a custom event (@update-category) 
  -->
  <Projects
    :projects="projectsData"
    :categories="categories" 
    :activeCategory="activeCategory"
    @update-category="setActiveCategory"
  />
  
  <About />
  <Skills />
  <Contact />
  <Footer/>

</template>

<script setup>
// React's `useState` is replaced by Vue's `ref`
import { onMounted, inject, ref, watch } from 'vue'
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
const api = inject("api");
const endpoints = inject('endpoints');

// State management
const projectsData = ref({ projects: [] })
const categories = ref([])
const activeCategory = ref('')

// The state updater function
const setActiveCategory = (newCategory) => {
  activeCategory.value = newCategory // In Vue, you mutate the .value of a ref
}

onMounted(() =>{
  loadCategories();
})

let loadTimeout = null;
// Watch activeCategory and fetch projects whenever it changes with a delay for exit animation
watch(activeCategory, (newCategory) => {
  if (newCategory) {
    if (loadTimeout) clearTimeout(loadTimeout);
    loadTimeout = setTimeout(() => {
      if(newCategory == "All"){
        loadAllProjects();
      }else{
        loadProjects(newCategory);
      }
    }, 250); // Delay to allow the cards exit animation to complete
  }
})

async function loadAllProjects(){
  try {
    const response = await api.get(endpoints.PROJECTS)
    if (response.status === 200) {
      projectsData.value = response.data;
    }
  } catch (error) {
    console.error('Error fetching projects:', error)
  }
}

async function loadProjects(category){
  try {
    if (!category) return;
    const response = await api.get(endpoints.PROJECTS, { params: { category: category } })
    if (response.status === 200) {
      projectsData.value = response.data;
      console.log(`Projects fetched: ${category}`);
      console.log(projectsData.value);
    }
  } catch (error) {
    console.error('Error fetching projects:', error)
  }
}

async function loadCategories(){
  try{
    const response = await api.get(`${endpoints.CATEGORIES}`)
    if(response.status == 200){
      categories.value = response.data;    
      categories.value = [...categories.value, {id: 0, name: "All"}];
      if (categories.value.length > 0 && !activeCategory.value) {
        activeCategory.value = categories.value[0].name;
      }
    }
  }catch (error){
    console.error('Error fetching categories:', error);
  }
}
</script>