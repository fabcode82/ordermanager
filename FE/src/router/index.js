import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import OrderEditView from '../views/OrderEditView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
  {
    path: '/order/:id',
    name: 'OrderEdit',
    component: OrderEditView,
    props: true,
  },
  ],
})

export default router
