import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router'
import './styles/style.scss'
// import { i18n } from "@/utils/i18n.js";


const app = createApp(App);
// app.use(i18n);
app.use(router);
app.mount("#app");