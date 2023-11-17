<template>
  <v-app>
    <v-main>
      <v-container>
        <v-card>
          <v-card-title>Login with Shopify</v-card-title>
          <v-card-text>
            <v-text-field v-model="shopName" label="Shop Name" />
            <v-btn color="primary" @click="loginWithShopify">Login</v-btn>
          </v-card-text>
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from 'vue'
import { getShopifyAuthUrl } from '@/api/auth'

const shopName = ref('')

const loginWithShopify = async () => {
  const redirectTo = await getShopifyAuthUrl({
    shop: shopName.value,
  })
  window.location.href = redirectTo
}
</script>
