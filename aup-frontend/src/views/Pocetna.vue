<script setup lang="ts">
import {ref, onMounted} from "vue";

const fakultet = ref("Test");
const profesori = ref([]);
const headers = [
  {title: 'ID', value: 'id'},
  {title: 'E-pošta', value: 'email'},
  {title: 'Ime', value: 'ime'},
  {title: 'Prezime', value: 'prezime'},
]

async function dohvatiProfesore() {
  const response = await fetch('http://localhost:5005/profesori')
  const data = await response.json()

  profesori.value = data
}

onMounted(async () => {
  // await dohvatiProfesore()
})


</script>

<template>
  Početna stranica. <br>

  <v-text-field
      hint="Ovo je hint"
      append-inner-icon="mdi-shield-lock-open-outline"
      persistent-hint
      v-model="fakultet"
      v-if="fakultet.length < 10"
  >

  </v-text-field>
  <v-btn text="Dohvati profesore" @click="dohvatiProfesore"></v-btn>

  <p>
    Fakultet: {{ fakultet }}
  </p>


  <br>

  <v-data-table :headers="headers" :items="profesori"></v-data-table>

  <br>

  <v-row>
    <v-col v-for="profesor in profesori" sm="12" md="6" lg="4" xl="3">
      <v-card>
        <v-card-text>
          <h1>{{ profesor.ime + " " + profesor.prezime }}</h1>

          <p>{{ profesor.email }}</p>

          <p>{{ profesor.titula }}</p>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>


  <ol>
    <li v-for="broj in [1, 5, 7, 51, 12]">Prva stavka {{ broj }}</li>
  </ol>

  <br>

  <p v-if="profesori.length > 0">{{ profesori }}</p>
</template>

<style scoped>

</style>