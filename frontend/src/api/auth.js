import api from '.'
export async function getShopifyAuthUrl(data) {
  return await api.post('/auth/shopify_auth_url', data)
}
export async function sendShopifyAuth(data) {
  return await api.post('/auth/shopify_callback', data)
}
