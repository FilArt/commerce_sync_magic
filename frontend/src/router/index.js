// Composables
import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/store/auth'

const isAuthenticated = () => useAuthStore().isAuthenticated

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/login'),
  },
  {
    path: '/auth',
    name: 'Auth',
    component: () => import('@/views/auth'),
  },
  {
    path: '/',
    component: () => import('@/layouts/default'),
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (Home-[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import('@/views/home'),
      },
      {
        path: '/settings',
        name: 'Settings',
        component: () => import('@/views/settings'),
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

router.beforeEach((to, from, next) => {
  if (!isAuthenticated() && !['Login', 'Auth'].includes(to.name)) {
    next({ name: 'Login' })
  } else {
    next()
  }
})

export default router
