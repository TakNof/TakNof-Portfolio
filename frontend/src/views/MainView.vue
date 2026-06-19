<template>
  <div class="main-layout">
    <!-- Header and Footer can go here if they are on every page, 
         or inside Home if they are ONLY on the Home page. 
         Based on your structure, they are in Home. -->
    
    <!-- router-view renders Home or ProjectDetail depending on the URL -->
    <router-view />
  </div>
</template>