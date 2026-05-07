import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'

const Pocetna = () => import('@/views/pages/Pocetna.vue')
const Profesori = () => import('@/views/profesori/Profesori.vue')
const ProfesorForma = () => import('@/views/profesori/ProfesorForma.vue')
const ProfesorPregled = () => import('@/views/profesori/ProfesorPregled.vue')
const Kolegiji = () => import('@/views/kolegiji/Kolegiji.vue')
const KolegijForma = () => import('@/views/kolegiji/KolegijForma.vue')

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'Pocetna',
    component: Pocetna,
  },
  {
    path: '/profesori',
    name: 'Profesori',
    component: Profesori,
  },
  {
    path: '/profesori/dodaj',
    name: 'ProfesorDodaj',
    component: ProfesorForma,
  },
  {
    path: '/profesori/:id',
    name: 'ProfesorPregled',
    component: ProfesorPregled,
  },
  {
    path: '/profesori/:id/uredi',
    name: 'ProfesorUredi',
    component: ProfesorForma,
  },
  {
    path: '/kolegiji',
    name: 'Kolegiji',
    component: Kolegiji,
  },
  {
    path: '/kolegiji/dodaj',
    name: 'KolegijDodaj',
    component: KolegijForma,
  },
  {
    path: '/kolegiji/:id/uredi',
    name: 'KolegijUredi',
    component: KolegijForma,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
