import { createRouter, createWebHashHistory } from 'vue-router'

const MainView = () => import(/* webpackChunkName: "main" */ '@/views/MainView.vue');
const Home = () => import(/*webpackChunkName: "home"*/ '@/views/Home.vue');
const ProjectDetail = () => import(/*webpackChunkName: "project-detail*/ '@/views/ProjectDetail.vue');

const routes = [
  {
    path: '',
    component: MainView,
    children: [
      {
        path: '',
        component: Home
      },
      {
        path: '/project/:id',
        component: ProjectDetail
      }
    ]
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth', // This gives you the smooth animation
        top: 80 // Optional: adds an 80px offset if you have a sticky navbar!
      }
    }
    if (savedPosition) {
      return savedPosition
    }
    return { top: 0 } // Scroll to top by default on page change
  }
})

export default router