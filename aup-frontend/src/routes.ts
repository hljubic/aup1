import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'

const Pocetna = () => import('@/views/Pocetna.vue')
const ONama = () => import('@/views/ONama.vue')
const Kontakt = () => import('@/views/Kontakt.vue')


const routes: RouteRecordRaw[] = [
    {
        path: '/',
        name: 'Pocetna',
        component: Pocetna,
    },
    {
        path: '/o-nama',
        name: 'ONama',
        component: ONama,
    },
    {
        path: '/kontakt',
        name: 'Kontakt',
        component: Kontakt,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router