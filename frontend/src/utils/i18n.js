import { createI18n } from "vue-i18n";
import messages from "@/locales/locales.js";

export const i18n = createI18n({
    locale: "en", // Default language
    fallbackLocale: "en", // Fallback language
    legacy: false, // Use Composition API
    messages, // Translation messages
});