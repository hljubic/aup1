<script setup lang="ts">
import {reactive} from "vue";

const profesor = reactive({
  ime: '',
  prezime: '',
  email: '',
  titula: ''
})

async function spremiProfesora() {
  const response = await fetch('http://localhost:5005/profesori', {
    method: 'POST',
     headers: {
     'Content-Type': 'application/json'
    },
    body: JSON.stringify(profesor)
  })

  const data = await response.json()
}
</script>

<template>
  <v-text-field v-model="profesor.ime"
                label="Ime.."></v-text-field>
  <v-text-field v-model="profesor.prezime"
                label="Prezime.."></v-text-field>
  <v-text-field v-model="profesor.email"
                label="E-pošta.."></v-text-field>
  <v-text-field v-model="profesor.titula"
                label="Titula.."></v-text-field>

  <v-btn text="Spremi" @click="spremiProfesora"></v-btn>
</template>

<style scoped>

</style>