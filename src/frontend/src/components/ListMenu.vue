<template>
  <div>
    <list-items :items="items"></list-items>
    <create-list-item :colors="colors" v-on:create="get_items"></create-list-item>
  </div>
</template>

<script>
import ListItems from "@/components/ListItems";
import CreateListItem from "@/components/CreateListItem";
import {httpClient} from "@/http-client";

export default {
  name: 'ListMenu',
  components: {
    ListItems,
    CreateListItem
  },
  data() {
    return {
      items: [],
      colors: []
    }
  },
  methods: {
    async get_items() {
      const result = (await httpClient().get('/list_item')).data
      this.items = result.items
      console.log(this.items)

    }
  },
  async mounted() {
    await this.get_items()
    const colors = (await httpClient().get('/color')).data
    this.colors = colors
  },
}
</script>