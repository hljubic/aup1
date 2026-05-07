<script setup lang="ts">
import { computed, onMounted, reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const API_URL = 'http://localhost:5005'

const route = useRoute()
const router = useRouter()
const loading = ref(false)

const profesor = reactive<any>({
  ime: '',
  prezime: '',
  email: '',
  titula: '',
})

const jeUredivanje = computed(() => !!route.params.id)
const naslov = computed(() => jeUredivanje.value ? 'Uredi profesora' : 'Dodaj profesora')
const tekstGumba = computed(() => jeUredivanje.value ? 'Spremi promjene' : 'Spremi profesora')

async function dohvatiProfesora() {
  if (!route.params.id) {
    return
  }

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

async function spremiProfesora() {
  loading.value = true

  const url = jeUredivanje.value
    ? `${API_URL}/profesori/${route.params.id}`
    : `${API_URL}/profesori`

  const method = jeUredivanje.value ? 'PUT' : 'POST'

  try {
    await fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(profesor),
    })

    router.push('/profesori')
  } catch (error) {
    console.log(error)
  }

  loading.value = false
}

function odustani() {
  router.push('/profesori')
}

onMounted(async () => {
  await dohvatiProfesora()
})
</script>

<template>
  <v-card max-width="700">
    <v-card-title>
      {{ naslov }}
    </v-card-title>

    <v-card-text>
      <v-text-field
        v-model="profesor.ime"
        label="Ime"
        prepend-inner-icon="mdi-account"
      />

      <v-text-field
        v-model="profesor.prezime"
        label="Prezime"
        prepend-inner-icon="mdi-account-outline"
      />

      <v-text-field
        v-model="profesor.email"
        label="E-pošta"
        prepend-inner-icon="mdi-email-outline"
      />

      <v-text-field
        v-model="profesor.titula"
        label="Titula"
        prepend-inner-icon="mdi-school-outline"
      />
    </v-card-text>

    <v-card-actions>
      <v-spacer />

      <v-btn
        variant="text"
        @click="odustani"
      >
        Odustani
      </v-btn>

      <v-btn
        color="primary"
        :loading="loading"
        @click="spremiProfesora"
      >
        {{ tekstGumba }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>
