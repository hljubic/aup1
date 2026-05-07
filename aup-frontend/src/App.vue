<template>
  <v-app>
    <v-app-bar flat>
      <v-container class="mx-auto d-flex align-center">
        <div class="text-h6 font-weight-bold">
          Algoritmi u primjeni
        </div>

        <v-spacer />

        <v-btn
          v-for="link in links"
          :key="link.link"
          :to="link.link"
          variant="text"
        >
          {{ link.text }}
        </v-btn>
      </v-container>
    </v-app-bar>

    <v-main class="bg-grey-lighten-3">
      <v-container class="py-6">
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
const links = [
  {
    link: '/',
    text: 'Početna',
  },
  {
    link: '/profesori',
    text: 'Profesori',
  },
  {
    link: '/kolegiji',
    text: 'Kolegiji',
  },
]
</script>
