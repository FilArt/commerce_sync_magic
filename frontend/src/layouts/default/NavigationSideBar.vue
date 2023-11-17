<template>
  <v-list nav>
    <v-list-item
      v-for="link in links"
      :key="link.to"
      :value="link.to"
      :title="link.title"
      :to="link.to"
      exact
      color="primary"
    >
      <template v-slot:prepend>
        <v-icon :icon="link.icon"></v-icon>
      </template>
    </v-list-item>
  </v-list>
</template>

<script>
export default {
  data: () => ({
    links: [
      {
        title: 'Dashboard',
        icon: 'mdi-view-dashboard',
        to: '/',
      },
      {
        title: 'Settings',
        icon: 'mdi-cog',
        to: '/settings',
      },
    ],
  }),
}
</script>
