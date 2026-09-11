export const ENDPOINTS = Object.freeze({
    // Static Routes
    PROJECTS: '/projects/',
    PROJECTS_BY_IDS: '/projects/by-ids',
    CATEGORIES: '/categories/',
    TECH_SKILLS: '/skills/',
    TECHS: '/techs/',
    TECH_BRANCHES: '/tech-branches/',

    // Dynamic Routes (Using a function to inject the ID)
    PROJECT_DETAIL: (id) => `/projects/${id}`,
})