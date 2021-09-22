<template>
  <v-list-item>
    <v-icon @click="show = !show">{{ show ? 'mdi-minus-circle' : 'mdi-plus-circle' }}</v-icon>
    <v-list-item-content>
      <v-list-item-title class="mx-2">Добавить список</v-list-item-title>
    </v-list-item-content>
    <div v-show="show" class="mx-2">

      <v-text-field @keydown.enter="create_item(), $emit('create')"
          label="Название списка"
          v-model="new_item.name"
      ></v-text-field>
      <v-btn @click="create_item(), $emit('create')"
              x-small
              color="primary"

      >Добавить</v-btn>
    </div>
  </v-list-item>
</template>

<script>
import {httpClient} from "@/http-client";

export default {
  name: 'CreateListItem',
  props: {
    colors: Array
  },
  data() {
    return {
      show: false,
      new_item: {
        name: '',
        color: ''
      }

    }
  },
  methods: {
    async create_item() {
      const rand = Math.floor(Math.random() * this.colors.length);
      this.new_item.color = this.colors[rand]
      const result = (await httpClient().post('/list_item', this.new_item))
      if (result.statusText == 'OK') {
        this.new_item.color = ''
        this.new_item.name = ''
      }
    }
  }
}
</script>