<template>
  <v-list-item-group
      v-model="selectedItem"
      color="primary"
  >
    <v-list-item v-for="item in items" :key="item.id" @click="goToListItem(item.id)">
        <v-list-item-avatar :color="item.color" size="20">
        </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title v-text="item.name"></v-list-item-title>
        <v-list-item-subtitle v-text="item.created_on"></v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
  </v-list-item-group>
</template>

<script>

export default {
  name: 'ListItems',
  props: ['items'],
  data() {
    return {
      selectedItem: 0
    }
  },
  watch: {
    selectedItem: function () {
      //console.log(this.selectedItem//
    }
  },
  methods: {
    goToListItem (item_id) {
      //const item = this.items[this.selectedItem]
      this.$router.push(
          {
            path: `/${item_id}`
          }
      )
    }
  }
}
</script>