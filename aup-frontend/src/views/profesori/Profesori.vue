<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

const API_URL = 'http://localhost:5005'

const router = useRouter()
const loading = ref(false)
const prikazi_dialog_brisanje = ref(false)
const profesori = ref<any[]>([])
const profesor_za_brisanje = ref<any>(null)
const pretraga = ref('')

const headers = [
  { title: 'ID', value: 'id' },
  { title: 'Ime', value: 'ime' },
  { title: 'Prezime', value: 'prezime' },
  { title: 'E-pošta', value: 'email' },
  { title: 'Titula', value: 'titula' },
  { title: 'Akcije', key: 'actions', sortable: false },
]

async function dohvatiProfesore() {
  loading.value = true

  try {
    const response = await fetch(`${API_URL}/profesori?q=${encodeURIComponent(pretraga.value)}`)
    profesori.value = await response.json()
  } catch (error) {
    console.log(error)
  }

  loading.value = false
}

function idiNaDodavanje() {
  router.push('/profesori/dodaj')
}

async function pretraziProfesore() {
  await dohvatiProfesore()
}

function pregledaj(profesor: any) {
  router.push(`/profesori/${profesor.id}`)
}

function uredi(profesor: any) {
  router.push(`/profesori/${profesor.id}/uredi`)
}

function otvoriBrisanje(profesor: any) {
  profesor_za_brisanje.value = profesor
  prikazi_dialog_brisanje.value = true
}

function zatvoriBrisanje() {
  profesor_za_brisanje.value = null
  prikazi_dialog_brisanje.value = false
}

async function obrisiProfesora() {
  if (!profesor_za_brisanje.value) {
    return
  }

  loading.value = true

  try {
    await fetch(`${API_URL}/profesori/${profesor_za_brisanje.value.id}`, {
      method: 'DELETE',
    })

    await dohvatiProfesore()
  } catch (error) {
    console.log(error)
  }

  loading.value = false
  zatvoriBrisanje()
}

onMounted(async () => {
  await dohvatiProfesore()
})
</script>

<template>
  <v-card>
    <v-card-title class="d-flex align-center">
      Profesori

      <v-spacer />

      <v-btn
        color="primary"
        prepend-icon="mdi-plus"
        @click="idiNaDodavanje"
      >
        Dodaj
      </v-btn>
    </v-card-title>

    <v-card-text>
      <v-text-field
        v-model="pretraga"
        label="Pretraži profesore"
        prepend-inner-icon="mdi-magnify"
        clearable
        class="mb-4"
        @update:model-value="pretraziProfesore"
      />

      <v-data-table
        :headers="headers"
        :items="profesori"
        :loading="loading"
      >
        <template #item.actions="{ item }">
          <v-tooltip text="Pregledaj">
            <template #activator="{ props }">
              <v-btn
                v-bind="props"
                icon="mdi-eye"
                size="small"
                variant="text"
                @click="pregledaj(item)"
              />
            </template>
          </v-tooltip>

          <v-tooltip text="Uredi">
            <template #activator="{ props }">
              <v-btn
                v-bind="props"
                icon="mdi-pencil"
                size="small"
                variant="text"
                @click="uredi(item)"
              />
            </template>
          </v-tooltip>

          <v-tooltip text="Obriši">
            <template #activator="{ props }">
              <v-btn
                v-bind="props"
                icon="mdi-delete"
                size="small"
                variant="text"
                @click="otvoriBrisanje(item)"
              />
            </template>
          </v-tooltip>
        </template>
      </v-data-table>
    </v-card-text>
  </v-card>

  <v-dialog
    v-model="prikazi_dialog_brisanje"
    max-width="500"
  >
    <v-card>
      <v-card-title>
        Potvrda brisanja
      </v-card-title>

      <v-card-text>
        Jeste li sigurni da želite obrisati profesora?
      </v-card-text>

      <v-card-actions>
        <v-spacer />

        <v-btn
          variant="text"
          @click="zatvoriBrisanje"
        >
          Odustani
        </v-btn>

        <v-btn
          color="red"
          :loading="loading"
          @click="obrisiProfesora"
        >
          Obriši
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
