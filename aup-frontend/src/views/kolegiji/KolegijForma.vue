<script setup lang="ts">
import { computed, onMounted, reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const API_URL = 'http://localhost:5005'

const route = useRoute()
const router = useRouter()
const loading = ref(false)
const profesori = ref<any[]>([])

const kolegij = reactive<any>({
  naziv: '',
  ects: '',
  semestar: '',
  nositelj_id: '',
})

const jeUredivanje = computed(() => !!route.params.id)
const naslov = computed(() => jeUredivanje.value ? 'Uredi kolegij' : 'Dodaj kolegij')
const tekstGumba = computed(() => jeUredivanje.value ? 'Spremi promjene' : 'Spremi kolegij')

async function dohvatiKolegij() {
  if (!route.params.id) {
    return
  }

  loading.value = true

  try {
    const response = await fetch(`${API_URL}/kolegiji/${route.params.id}`)
    const data = await response.json()
    Object.assign(kolegij, data)
  } catch (error) {
    console.log(error)
  }

  loading.value = false
}

async function dohvatiProfesore() {
  try {
    const response = await fetch(`${API_URL}/profesori-dropdown`)
    profesori.value = await response.json()
  } catch (error) {
    console.log(error)
  }
}

function pripremiPodatke() {
  return {
    naziv: kolegij.naziv,
    ects: kolegij.ects === '' ? null : Number(kolegij.ects),
    semestar: kolegij.semestar === '' ? null : Number(kolegij.semestar),
    nositelj_id: kolegij.nositelj_id === '' ? null : Number(kolegij.nositelj_id),
  }
}

async function spremiKolegij() {
  loading.value = true

  const url = jeUredivanje.value
    ? `${API_URL}/kolegiji/${route.params.id}`
    : `${API_URL}/kolegiji`

  const method = jeUredivanje.value ? 'PUT' : 'POST'

  try {
    await fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(pripremiPodatke()),
    })

    router.push('/kolegiji')
  } catch (error) {
    console.log(error)
  }

  loading.value = false
}

function odustani() {
  router.push('/kolegiji')
}

onMounted(async () => {
  await dohvatiProfesore()
  await dohvatiKolegij()
})
</script>

<template>
  <v-card max-width="700">
    <v-card-title>
      {{ naslov }}
    </v-card-title>

    <v-card-text>
      <v-text-field
        v-model="kolegij.naziv"
        label="Naziv"
        prepend-inner-icon="mdi-book-open-page-variant-outline"
      />

      <v-text-field
        v-model="kolegij.ects"
        label="ECTS"
        type="number"
        prepend-inner-icon="mdi-counter"
      />

      <v-text-field
        v-model="kolegij.semestar"
        label="Semestar"
        type="number"
        prepend-inner-icon="mdi-calendar-range"
      />

      <v-select
        v-model="kolegij.nositelj_id"
        :items="profesori"
        label="Nositelj"
        prepend-inner-icon="mdi-account-tie-outline"
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
        @click="spremiKolegij"
      >
        {{ tekstGumba }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>
