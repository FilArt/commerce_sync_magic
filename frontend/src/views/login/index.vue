<template>
  <v-app>
    <v-main>
      <v-container class="d-flex flex-column text-center">
        <v-form @submit.prevent="loginWithShopify">
          <v-card class="ma-auto pa-2" max-width="750" min-width="500">
            <v-card-title> Login </v-card-title>
            <v-card-text>
              <v-text-field v-model="shopName" label="Shop Name" name="shop" />
              <v-alert variant="outlined" type="info">
                You will be redirected to Shopify to login
              </v-alert>
            </v-card-text>
            <v-card-actions>
              <v-btn
                block
                color="primary"
                append-icon="mdi-login"
                type="submit"
              >
                Login with Shopify
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-form>
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
