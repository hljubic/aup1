<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

const API_URL = 'http://localhost:5005'

const router = useRouter()
const loading = ref(false)
const prikazi_dialog_brisanje = ref(false)
const kolegiji = ref<any[]>([])
const kolegij_za_brisanje = ref<any>(null)
const page = ref(1)
const per_page = ref(10)
const total = ref(0)
const pretraga = ref('')

const headers = [
  { title: 'ID', value: 'id' },
  { title: 'Naziv', value: 'naziv' },
  { title: 'ECTS', value: 'ects' },
  { title: 'Semestar', value: 'semestar' },
  { title: 'Nositelj', value: 'nositelj_ime_prezime' },
  { title: 'Akcije', key: 'actions', sortable: false },
]

async function dohvatiKolegije() {
  loading.value = true

  try {
    const response = await fetch(`${API_URL}/kolegiji?page=${page.value}&per_page=${per_page.value}&q=${encodeURIComponent(pretraga.value)}`)
    const data = await response.json()

    kolegiji.value = data.items
    page.value = data.page
    per_page.value = data.per_page
    total.value = data.total
  } catch (error) {
    console.log(error)
  }

  loading.value = false
}

function idiNaDodavanje() {
  router.push('/kolegiji/dodaj')
}

async function pretraziKolegije() {
  page.value = 1
  await dohvatiKolegije()
}

async function promijeniOpcije(opcije: any) {
  page.value = opcije.page
  per_page.value = opcije.itemsPerPage
  await dohvatiKolegije()
}

function uredi(kolegij: any) {
  router.push(`/kolegiji/${kolegij.id}/uredi`)
}

function otvoriBrisanje(kolegij: any) {
  kolegij_za_brisanje.value = kolegij
  prikazi_dialog_brisanje.value = true
}

function zatvoriBrisanje() {
  kolegij_za_brisanje.value = null
  prikazi_dialog_brisanje.value = false
}

async function obrisiKolegij() {
  if (!kolegij_za_brisanje.value) {
    return
  }

  loading.value = true

  try {
    await fetch(`${API_URL}/kolegiji/${kolegij_za_brisanje.value.id}`, {
      method: 'DELETE',
    })

    await dohvatiKolegije()
  } catch (error) {
    console.log(error)
  }

  loading.value = false
  zatvoriBrisanje()
}

onMounted(async () => {
  await dohvatiKolegije()
})
</script>

<template>
  <v-card>
    <v-card-title class="d-flex align-center">
      Kolegiji

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
        label="Pretraži kolegije"
        prepend-inner-icon="mdi-magnify"
        clearable
        class="mb-4"
        @update:model-value="pretraziKolegije"
      />

      <v-data-table-server
        v-model:page="page"
        v-model:items-per-page="per_page"
        :headers="headers"
        :items="kolegiji"
        :items-length="total"
        :loading="loading"
        :items-per-page-options="[5, 10, 15]"
        @update:options="promijeniOpcije"
      >
        <template #item.actions="{ item }">
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
      </v-data-table-server>
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
        Jeste li sigurni da želite obrisati kolegij?
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
          @click="obrisiKolegij"
        >
          Obriši
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
