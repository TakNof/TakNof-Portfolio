import axios from 'axios'

// Create a custom Axios instance
const api = axios.create({
  baseURL: import.meta.env.VITE_BACKEND_URL,
  
  timeout: 10000, 
  headers: {
    'Content-Type': 'application/json'
  }
})

export default api