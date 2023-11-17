import api from '.'

export function fetchCustomerData() {
  return api.get('/customer/me')
}
