<template>
  <!-- App.vue -->

  <v-app>
    <v-navigation-drawer app
                         v-model="drawer"
                         absolute
                         top
                         temporary>
      <user-card></user-card>
      <list-menu></list-menu>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon
          @click="drawer=!drawer"
      ></v-app-bar-nav-icon>

      <v-toolbar-title>Простой список дел</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container >
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>

</template>

<script>
import ListMenu from './components/ListMenu';
import UserCard from './components/UserCard.vue';

export default {
  name: 'App',

  components: {
    ListMenu,
    UserCard
  },

  data: () => ({
    drawer: true
  }),
};
</script>
