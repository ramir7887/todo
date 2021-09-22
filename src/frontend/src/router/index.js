import Vue from 'vue'
import VueRouter from 'vue-router'
import ListItemView from "@/components/ListItemView";

Vue.use(VueRouter)

const routes = [
  {
    path: '/:item_id',
    name: 'Home',
    component: ListItemView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
