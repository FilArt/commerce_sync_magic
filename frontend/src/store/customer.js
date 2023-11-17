import { fetchCustomerData } from '@/api/customer'
import { defineStore } from 'pinia'

export const useCustomerStore = defineStore('customer', {
  state: () => ({
    customerData: {},
    shopify: {},
  }),
  actions: {
    async refresh() {
      const data = await fetchCustomerData()
      this.customerData = data
    },
  },
})
