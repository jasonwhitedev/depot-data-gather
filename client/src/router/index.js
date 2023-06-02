import { createRouter, createWebHistory } from 'vue-router'
import Depots from '../components/Depots.vue'
import Forms from '../components/AddDepot.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Depots',
      component: Depots,
    },
    {
      path: '/forms',
      name: 'Forms',
      component: Forms,
    },
  ]
})

export default router
