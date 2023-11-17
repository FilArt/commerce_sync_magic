import api from '.'
export async function getShopifyAuthUrl(data) {
  return await api.post('/auth/shopify_auth_url', data)
}
