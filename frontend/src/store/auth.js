import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: null,
  }),
  getters: {
    isAuthenticated(state) {
      return !!state.token
    },
  },
})
