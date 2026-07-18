<template>
  <section id="contact-me" class="section">
    <div class="section-title">
      <h2>Let's Work Together!</h2>
      <div class="title-line"></div>
    </div>
    
    <div class="contact-content">
      <p class="contact-subtitle">
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

<style lang="scss" scoped>
.contact-content {
  max-width: 650px;
  margin: 0 auto;
  padding: 0 1rem;
}

.contact-subtitle {
  text-align: center;
  color: $text-secondary;
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 3rem;
}

.contact-form {
  @include glass-panel($bg-card, $border-color, 16px);
  padding: 3rem;
  border-radius: $border-radius-lg;
  box-shadow: $shadow-lg;
  display: flex;
  flex-direction: column;
  gap: 1.75rem;

  @include mobile {
    padding: 1.5rem;
  }
}

.form-group {
  display: flex;
  flex-direction: column;
  text-align: left;
  gap: 0.5rem;
}

label {
  font-family: $font-heading;
  font-size: 0.85rem;
  font-weight: 600;
  color: $text-primary;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

input, textarea {
  background: rgba(255, 255, 255, 0.015);
  border: 1px solid $border-color;
  border-radius: $border-radius-md;
  padding: 0.85rem 1.1rem;
  color: $text-primary;
  font-family: $font-sans;
  font-size: 0.95rem;
  transition: $transition-normal;
  width: 100%;
  box-sizing: border-box;
  
  &::placeholder {
    color: $text-muted;
  }
  
  &:focus {
    outline: none;
    border-color: $color-dev;
    box-shadow: 0 0 0 3px rgba($color-dev, 0.15);
    background: rgba(255, 255, 255, 0.04);
  }
}

textarea {
  resize: vertical;
}

.submit-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 1rem;
  font-family: $font-heading;
  font-size: 1rem;
  font-weight: 700;
  border-radius: $border-radius-md;
  border: none;
  background: linear-gradient(135deg, $color-dev, $color-art);
  color: white;
  cursor: pointer;
  transition: $transition-normal;
  box-shadow: 0 4px 15px rgba($color-dev, 0.25);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  
  &:hover {
    background: linear-gradient(135deg, lighten($color-dev, 4%), lighten($color-art, 4%));
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba($color-dev, 0.4);
  }
  
  &:active {
    transform: translateY(0);
  }
}
</style>