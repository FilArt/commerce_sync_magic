<template>
  <v-layout class="rounded rounded-md">
    <v-app-bar title="Commerce sync magic">
      <template v-slot:prepend>
        <v-app-bar-nav-icon v-if="!drawer" @click="drawer = !drawer" />
      </template>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer">
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
    </v-navigation-drawer>

    <v-main
      class="d-flex align-center justify-center"
      style="min-height: 300px"
    >
      <router-view />
    </v-main>
  </v-layout>
</template>

<script>
export default {
  data: () => ({
    drawer: true,
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
