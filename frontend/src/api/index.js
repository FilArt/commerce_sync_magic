import { mande } from 'mande'

const baseURL = import.meta.env.DEV ? 'http://localhost:9000/api' : '/api'

const api = mande(baseURL, {
  headers: {
    'Content-Type': 'application/json',
  },
})

export function setToken(token) {
  // todos.options will be used for all requests
  api.options.headers.Authorization = 'Bearer ' + token
}

export function clearToken() {
  delete api.options.headers.Authorization
}

export default api
