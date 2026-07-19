import { ref } from 'vue'
import axios from 'axios'

// Create a custom Axios instance
const api = axios.create({
  baseURL: import.meta.env.VITE_BACKEND_URL,
  
  timeout: 10000, 
  headers: {
    'Content-Type': 'application/json'
  }
})

// Add reactive isLoading state to the api instance
api.isLoading = ref(false)

// Intercept requests to set isLoading to true
api.interceptors.request.use(
  (config) => {
    api.isLoading.value = true
    return config
  },
  (error) => {
    api.isLoading.value = false
    return Promise.reject(error)
  }
)

// Intercept responses to set isLoading to false
api.interceptors.response.use(
  (response) => {
    api.isLoading.value = false
    return response
  },
  (error) => {
    api.isLoading.value = false
    return Promise.reject(error)
  }
)

export default api