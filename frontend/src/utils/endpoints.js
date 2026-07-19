export const ENDPOINTS = Object.freeze({
    // Static Routes
    PROJECTS: '/projects/',
    CATEGORIES: '/categories/',
    TECH_TAGS: '/tags/',
    
    // Dynamic Routes (Using a function to inject the ID)
    PROJECT_DETAIL: (id) => `/projects/${id}`,
})