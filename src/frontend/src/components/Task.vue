<template>
  <v-card class="mt-2"
  >
    <v-container dense>
      <v-row class="px-2">
        <v-checkbox
            v-model="current_task.active"
            :disabled="!edit"
        ></v-checkbox>
        <v-text-field
            class="mt-2"
            v-model="current_task.name"
            label="Задача"
            :readonly="!edit"
        ></v-text-field>
        <v-card-subtitle>{{ current_task.created_on }}</v-card-subtitle>
      </v-row>
      <v-row>
        <v-col cols="10">
          <v-textarea
              rows="1"
              no-resize
              color="black"
              :readonly="!edit"
              label="Описание"
              v-model="current_task.description"
          ></v-textarea>
        </v-col>
        <v-col cols="auto">
          <v-row>
            <v-col v-if="edit">
              <v-btn @click="update_task"
                     fab
                     dark
                     small
                     color="green"
              >
                <v-icon>mdi-check</v-icon>
              </v-btn>
            </v-col>
            <v-col>
              <v-btn @click="change_mode"
                     fab
                     dark
                     small
                     color="primary"
              >
                <v-icon>{{ edit ? 'mdi-cancel' : 'mdi-pencil' }}</v-icon>
              </v-btn>
            </v-col>
            <v-col>
              <v-btn
                  @click="delete_task"
                  fab
                  dark
                  small
                  color="red"
              >
                <v-icon>mdi-delete</v-icon>
              </v-btn>
            </v-col>


          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import {httpClient} from "@/http-client";

export default {
  name: 'Task',
  props: ['task'],
  data() {
    return {
      completed: Boolean,
      edit: false,
      current_task: {
        name: '',
        description: '',
        created_on: '',
        active: '',
        id: null,
        list_item_id: null
      }

    }
  },
  mounted() {
    this.current_task = {
      name: this.task.name,
      description: this.task.description,
      created_on: this.task.created_on,
      active: this.task.active,
      id: this.task.id,
      list_item_id: this.task.list_item_id
    }
  },
  methods: {
    change_mode() {
      if (this.edit) {
        this.current_task = {
          name: this.task.name,
          description: this.task.description,
          created_on: this.task.created_on,
          active: this.task.active,
          id: this.task.id,
          list_item_id: this.task.list_item_id
        }
        this.edit = !this.edit
      } else {
        this.edit = !this.edit
      }
    },
    async update_task() {
      try {
        const result = (await httpClient().patch(`/task`, this.current_task)).statusText
        if (result == 'OK') {
          //this.task = this.current_task
          this.edit = false
          this.$emit('update')
        }
      } catch (error) {
        console.log(error)
        return []
      }
    },
    async delete_task() {
      try {
        const result = (await httpClient().delete(`/task/${this.current_task.id}`)).statusText
        if (result == 'OK') {
          //this.task = this.current_task
          this.$emit('update')
        }
      } catch (error) {
        console.log(error)
        return []
      }
    }
  }
}
</script>