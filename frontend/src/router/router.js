import { createRouter, createWebHistory } from 'vue-router'

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
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      const target = document.querySelector(to.hash)
      if (target) {
        return {
          top: target.getBoundingClientRect().top + window.scrollY - 80,
          behavior: 'smooth'
        }
      }
    }
    if (savedPosition) {
      return savedPosition
    }
    return { top: 0 }
  }
})

export default router