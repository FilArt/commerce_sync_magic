<template>
  <v-layout class="rounded rounded-md">
    <v-app-bar title="Commerce sync magic">
      <template v-slot:prepend>
        <v-app-bar-nav-icon icon="mdi-cart" />
      </template>
    </v-app-bar>

    <v-navigation-drawer>
      <navigation-side-bar />
    </v-navigation-drawer>

    <v-main>
      <router-view />
    </v-main>
  </v-layout>
</template>

<script setup>
import NavigationSideBar from './NavigationSideBar.vue'
</script>
