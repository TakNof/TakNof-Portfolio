<template>
  <Hero :projects="featuredProjects" />
  
  <Projects
    :projects="projectsData"
    :categories="categories" 
    :activeCategory="activeCategory"
    @update-category="setActiveCategory"
  />
  
  <About />
  <Skills />

  <Techs
    :techs="techsData"
    :branches="branches"
    :activeBranch="activeBranch"
    @update-branch="setActiveBranch"
  />

  <Contact />
  <Footer/>

</template>

<script setup>
// React's `useState` is replaced by Vue's `ref`
import { onMounted, inject, ref, watch } from 'vue';

// Import components (Make sure to add the .vue extension!)
import Header from '@/components/general/Header.vue'
import Hero from '@/components/general/Hero.vue'
import Projects from '@/components/general/Projects.vue'
import Skills from '@/components/general/Skills.vue'
import Techs from '@/components/general/Techs.vue'
import About from '@/components/general/About.vue'
import Contact from '@/components/general/Contact.vue'
import Footer from '@/components/general/Footer.vue'

// Import your JSON (Vite handles JSON imports perfectly)
const api = inject("api");
const endpoints = inject('endpoints');

// State management
const projectsData = ref({ projects: [] })   // category-filtered list for the Projects section
const featuredProjects = ref([])              // fixed set that powers the Hero carousel
const categories = ref([])
const activeCategory = ref('')

// Tech-stack state
const techsData = ref([])
const branches = ref([])
const activeBranch = ref('')

const FEATURED_PROJECT_IDS = [4, 1, 5, 13, 9, 3, 14];

// The state updater functions
const setActiveCategory = (newCategory) => {
  activeCategory.value = newCategory // In Vue, you mutate the .value of a ref
}

const setActiveBranch = (newBranch) => {
  activeBranch.value = newBranch
}

onMounted(() =>{
  loadFeaturedProjects();
  loadCategories();
  loadBranches();
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

async function loadFeaturedProjects(){
  if (!FEATURED_PROJECT_IDS.length) return;
  try {
    const response = await api.get(endpoints.PROJECTS_BY_IDS, {
      params: { ids: FEATURED_PROJECT_IDS.join(',') }
    })
    if (response.status === 200) {
      featuredProjects.value = response.data;
    }
  } catch (error) {
    console.error('Error fetching featured projects:', error)
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

let branchTimeout = null;
// Fetch techs whenever the active branch changes, with a delay for the exit animation.
watch(activeBranch, (newBranch) => {
  if (!newBranch) return;
  if (branchTimeout) clearTimeout(branchTimeout);
  branchTimeout = setTimeout(() => {
    if (newBranch === "All") {
      loadAllTechs();
    } else {
      loadTechs(newBranch);
    }
  }, 250);
})

async function loadAllTechs(){
  try {
    const response = await api.get(endpoints.TECHS)
    if (response.status === 200) {
      techsData.value = response.data;
    }
  } catch (error) {
    console.error('Error fetching techs:', error)
  }
}

async function loadTechs(branch){
  try {
    if (!branch) return;
    const response = await api.get(endpoints.TECHS, { params: { branch: branch } })
    if (response.status === 200) {
      techsData.value = response.data;
    }
  } catch (error) {
    console.error('Error fetching techs:', error)
  }
}

async function loadBranches(){
  try {
    const response = await api.get(`${endpoints.TECH_BRANCHES}`)
    if (response.status === 200) {
      branches.value = [...response.data, { id: 0, name: "All" }];
      if (branches.value.length > 0 && !activeBranch.value) {
        activeBranch.value = branches.value.at(-1).name;
      }
    }
  } catch (error) {
    console.error('Error fetching tech branches:', error);
  }
}
</script>