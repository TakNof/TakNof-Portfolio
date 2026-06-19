<template>
  <section id="contact-me" class="section">
    <div class="contact-content">
      <h2>Let's work together!</h2>
      <p>
        Do you have a project in mind? I'd love to collaborate with you to
        create extraordinary digital experiences that make a difference.
      </p>
      
      <!-- 
        @submit.prevent stops the page from reloading when the form is submitted.
        It automatically calls the submitForm function instead.
      -->
      <form class="contact-form" @submit.prevent="submitForm">
        
        <div class="form-group">
          <!-- htmlFor becomes standard HTML for -->
          <label for="name">Name</label>
          <!-- v-model binds this input directly to formData.name -->
          <input type="text" id="name" v-model="formData.name" required />
        </div>
        
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="formData.email" required />
        </div>
        
        <div class="form-group">
          <label for="project">Kind of project</label>
          <input 
            type="text" 
            id="project" 
            v-model="formData.project" 
            placeholder="Videogame, Web Page, App, AR/VR, Audiovisual..."
          />
        </div>
        
        <div class="form-group">
          <label for="message">Message</label>
          <textarea id="message" v-model="formData.message" rows="5" required></textarea>
        </div>
        
        <button type="submit" class="submit-btn">Send message</button>
      </form>
    </div>
  </section>
</template>

<script setup>
// 'reactive' is like 'ref', but specifically designed for objects!
import { reactive } from 'vue'

// 1. Define the reactive state for the form
const formData = reactive({
  name: '',
  email: '',
  project: '',
  message: ''
})

// 2. Handle the form submission
const submitForm = () => {
  // Here is where you will eventually send the data to your Flask backend, 
  // or a service like Formspree / EmailJS!
  
  console.log("Sending message...", formData)
  
  alert("Thanks for your message! I'll get back to you soon.")
  
  // Optional: Clear the form after sending
  formData.name = ''
  formData.email = ''
  formData.project = ''
  formData.message = ''
}
</script>

<style scoped>
/* Add your form styles here */
</style>