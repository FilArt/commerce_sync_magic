<template>
  <v-container class="d-flex flex-row justify-space-around">
    <v-card>
      <v-card-title> Shopify </v-card-title>

      <v-card-text>
        <v-row>
          <v-col> Products: </v-col>

          <v-col>
            {{ customerStore }}
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-title> Other </v-card-title>
    </v-card>
  </v-container>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCustomerStore } from '@/store/customer'

const customerStore = useCustomerStore()

onMounted(async () => {
  await customerStore.refresh()
})
</script>
