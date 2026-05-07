<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const API_URL = 'http://localhost:5005'

const route = useRoute()
const router = useRouter()
const loading = ref(false)

const profesor = reactive<any>({
  id: '',
  ime: '',
  prezime: '',
  email: '',
  titula: '',
})

async function dohvatiProfesora() {
  loading.value = true

  try {
    const response = await fetch(`${API_URL}/profesori/${route.params.id}`)
    const data = await response.json()
    Object.assign(profesor, data)
  } catch (error) {
    console.log(error)
  }

  loading.value = false
}

function povratak() {
  router.push('/profesori')
}

function urediProfesora() {
  router.push(`/profesori/${route.params.id}/uredi`)
}

onMounted(async () => {
  await dohvatiProfesora()
})
</script>

<template>
  <v-card max-width="700">
    <v-card-title class="d-flex align-center">
      Pregled profesora

      <v-spacer />

      <v-btn
        color="primary"
        prepend-icon="mdi-pencil"
        @click="urediProfesora"
      >
        Uredi
      </v-btn>
    </v-card-title>

    <v-card-text v-if="!loading">
      <p><strong>ID:</strong> {{ profesor.id }}</p>
      <p><strong>Ime:</strong> {{ profesor.ime }}</p>
      <p><strong>Prezime:</strong> {{ profesor.prezime }}</p>
      <p><strong>E-pošta:</strong> {{ profesor.email }}</p>
      <p><strong>Titula:</strong> {{ profesor.titula }}</p>
    </v-card-text>

    <v-card-text v-else>
      Učitavanje...
    </v-card-text>

    <v-card-actions>
      <v-spacer />

      <v-btn
        variant="text"
        @click="povratak"
      >
        Natrag
      </v-btn>
    </v-card-actions>
  </v-card>
</template>
