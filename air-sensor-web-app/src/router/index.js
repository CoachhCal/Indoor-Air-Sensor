import { createWebHistory, createRouter } from "vue-router";

import HomeView from '@/views/HomeView.vue'
import AnalyticsView from '@/views/AnalyticsView.vue'

const routes = [
    { path: '/', component: HomeView},
    { path: '/analytics', component: AnalyticsView},
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router