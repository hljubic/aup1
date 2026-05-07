<script setup lang="ts">
import {ref, onMounted, reactive} from "vue";

const profesor = reactive({
  ime: '',
  prezime: '',
  email: '',
  titula: ''
})

const loading = ref(false)
const fakultet = ref("Test");
const prikazi_dialog = ref(false);
const profesori = ref([]);
const headers = [
  {title: 'ID', value: 'id'},
  {title: 'E-pošta', value: 'email'},
  {title: 'Ime', value: 'ime'},
  {title: 'Prezime', value: 'prezime'},
  { title: 'Akcije', key: 'actions', sortable: false },
]

async function dohvatiProfesore() {
  loading.value = true
  const response = await fetch('http://localhost:5005/profesori')
  const data = await response.json()
  loading.value = false

  profesori.value = data
}

async function urediProfesora() {
  loading.value = true
  const response = await fetch(`http://localhost:5005/profesori/${profesor.id}`, {
    method: 'PUT',
     headers: {
     'Content-Type': 'application/json'
    },
    body: JSON.stringify(profesor)
  })

  //const data = await response.json()

  loading.value = false
  dohvatiProfesore()
  prikazi_dialog.value = false
}

onMounted(async () => {
  // await dohvatiProfesore()
})

function pregledaj(profesor: any) {
  console.log('Pregledaj', profesor)
}

function uredi(odabrani_profesor: any) {
  prikazi_dialog.value = true
  Object.assign(profesor, odabrani_profesor)
  console.log('Uredi', profesor)
}

async function obrisi(profesor: any) {
  const response = await fetch(`http://localhost:5005/profesori/${profesor.id}`, {
    method: 'DELETE',
  })

  await dohvatiProfesore()
}

</script>

<template>
  Početna stranica. <br>

  <v-dialog v-model="prikazi_dialog" max-width="500">
    <v-card>
      <v-card-title>
        Uredi profesora
      </v-card-title>

      <v-card-text>
        <v-text-field
          v-model="profesor.ime"
          label="Ime"
        />

        <v-text-field
          v-model="profesor.prezime"
          label="Prezime"
        />

        <v-text-field
          v-model="profesor.email"
          label="E-pošta"
        />

        <v-text-field
          v-model="profesor.titula"
          label="Titula"
        />
      </v-card-text>

      <v-card-actions>
        <v-spacer />

        <v-btn
          text="Odustani"
          variant="text"
          @click="prikazi_dialog = false"
        />

        <v-btn
          text="Spremi"
          color="primary"
          :loading="loading"
          @click="urediProfesora"
        />
      </v-card-actions>
    </v-card>
  </v-dialog>

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

  <v-data-table :loading="loading" :headers="headers" :items="profesori">
     <template #item.actions="{ item }">


      <v-tooltip text="Pregledaj">
        <template #activator="{ props }">
          <v-btn
            v-bind="props"
            icon="mdi-eye"
            variant="text"
            size="small"
            @click="pregledaj(item)"
          />
        </template>
      </v-tooltip>

      <v-tooltip text="Uredi">
        <template #activator="{ props }">
          <v-btn
            v-bind="props"
            icon="mdi-pencil"
            variant="text"
            size="small"
            @click="uredi(item)"
          />
        </template>
      </v-tooltip>

      <v-tooltip text="Obriši">
        <template #activator="{ props }">
          <v-btn
            v-bind="props"
            icon="mdi-delete"
            variant="text"
            size="small"
            @click="obrisi(item)"
          />
        </template>
      </v-tooltip>

    </template>
  </v-data-table>

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