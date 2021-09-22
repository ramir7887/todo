<template>
  <v-card
      class="mx-1 my-1"
      max-width="400"
  >
    <v-card-actions>
      <v-list-item class="grow">
        <v-list-item-avatar
            size="60"
            color="grey darken-3">
          <v-img
              alt="img this"
              src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"
          ></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title>{{name}}</v-list-item-title>
          <v-list-item-subtitle>{{email}}</v-list-item-subtitle>
        </v-list-item-content>

      </v-list-item>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'UserCard',
  data() {
    return {
      name: 'Ramir Abdulov',
      email: 'ramir@mail.ru'
    }
  }
}
</script>