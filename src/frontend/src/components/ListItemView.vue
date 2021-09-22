<template>
  <div>
    <v-card class="mb-2" :color="item.color" dark min-height="100">
      <v-container dense>
        <v-row dense>
          <v-col cols="10">
            <v-card-title class="text-h5">
              {{ item.name }}
            </v-card-title>
            <v-card-subtitle>
              {{ item.created_on }}
            </v-card-subtitle>
          </v-col>
          <v-col class="d-flex justify-end">
            <v-btn
                @click="delete_item(item.id)"
                class="ma-auto"
                fab
                dark
                small
                color="red"
            >
              <v-icon>mdi-delete</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
    <v-divider></v-divider>
    <tasks-view></tasks-view>
    <v-card>

    </v-card>
  </div>
</template>

<script>
import {httpClient} from "@/http-client";
import TasksView from "@/components/TasksView";

export default {
  name: 'ListItemView',
  components: {TasksView},
  data() {
    return {
      item: {
        name: '',
        id: 0,
        color: '#FFFFFF',
        created_on: ''
      },
      tasks: []
    }
  },
  watch: {
    async $route(to, from) {
      if (to.path != from.path) {
        const item_id = to.params.item_id;
        const item = await this.get_item(item_id)
        this.item = item
      }
    }
  },
  async mounted() {
    const item_id = this.$route.params.item_id
    const item = await this.get_item(item_id)
    this.item = item
  },
  methods: {
    async get_item(item_id) {
      try {
        const result = (await httpClient().get(`/list_item/${item_id}`)).data
        if (!result) {
          await this.$router.push('/')
        }
        return await result
      } catch (error) {
        await this.$router.push('/')
      }
    },
    async delete_item(item_id) {
      const result = (await httpClient().delete(`/list_item/${item_id}`)).data
      return await result
    },
    async update_listview() {
      const item_id = this.$route.params.item_id
      const item = await this.get_item(item_id)
      this.item = item
    }
  }


}
</script>