<template>
  <div class="mt-2 " style="position: relative">
    <v-fab-transition>
      <v-btn
          v-show="!hidden"
          @click="hidden = !hidden"
          color="green"
          fab
          dark

          absolute
          top
          right
      >
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </v-fab-transition>
    <v-card
        v-show="hidden" class="mb-10"
    >
      <v-container dense>
        <v-row dense>
          <v-card-title>Создание новой задачи</v-card-title>
        </v-row>
        <v-row dense class="px-2">

          <v-text-field dense
                        class="mt-2"
                        label="Задача"
                        v-model="new_task.name"
          ></v-text-field>
        </v-row>
        <v-row dense>
          <v-col cols="10">
            <v-textarea dense
                        rows="1"
                        no-resize
                        color="black"
                        label="Описание"
                        v-model="new_task.description"
            ></v-textarea>
          </v-col>
          <v-col cols="auto">
            <v-row>
              <v-col>
                <v-btn
                    fab
                    dark
                    small
                    color="green"
                    @click="create_task"
                >
                  <v-icon>mdi-check</v-icon>
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                    @click="cancel_create"
                    fab
                    dark
                    small
                    color="primary"
                >
                  <v-icon>mdi-cancel</v-icon>
                </v-btn>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
    <task v-for="task in tasks" :key="task.id" :task="task" class="ma-1" @update="update_taskview">
    </task>
  </div>

</template>

<script>
import Task from "@/components/Task";
import {httpClient} from "@/http-client";

export default {
  name: 'TasksView',
  components: {Task},
  data() {
    return {
      item_id: 1,
      tasks: [],
      hidden: false,
      new_task: {
        name: "",
        description: "",
        active: true,
        list_item_id: this.$route.params.item_id
      }
    }
  },
  watch: {
    async $route() {
      const item_id = this.$route.params.item_id;
      this.item_id = item_id
      const tasks = await this.get_tasks(item_id)
      this.tasks = tasks
    }
  },
  async mounted() {
    const item_id = this.$route.params.item_id;
    this.item_id = item_id
    this.tasks = await this.get_tasks(this.item_id)
  },
  methods: {
    async get_tasks(item_id) {
      try {
        const result = (await httpClient().get(`/task/${item_id}`))
        if (result.statusText == 'OK') {
          return await result.data.items
        } else {
          return []
        }
      } catch (error) {
        console.log(error)
        return []
      }

    },
    async update_taskview() {
      const item_id = this.$route.params.item_id;
      this.item_id = item_id
      this.tasks = await this.get_tasks(this.item_id)
    },
    cancel_create() {
      this.new_task = {
        name: "",
        description: "",
        active: true,
        list_item_id: this.$route.params.item_id
      }
      this.hidden = !this.hidden
    },
    async create_task() {
      if (this.new_task.name) {
        try {
          const result = (await httpClient().post(`/task/`, this.new_task))
          if (result.statusText == 'OK') {
            this.cancel_create()
            this.update_taskview()
          }
        } catch (error) {
          console.log(error)
          return []
        }

      }
    }
  }
}
</script>