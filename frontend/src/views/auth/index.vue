<script setup>
import api from '@/api'
import { useRoute, useRouter } from 'vue-router'

const authParams = { ...useRoute().query }
if (!authParams.code || !authParams.shop) {
  useRouter().replace({ name: 'Login' })
} else {
  useRouter().replace({ params: {} })
  api
    .post('/auth/shopify_callback', authParams)
    .then((data) => {
      useRouter().replace({ name: 'Home' })
    })
    .catch((error) => {
      console.error(error)
      alert('Authenticacion failed')
    })
}
</script>
