import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import * as routesData from './routes.json'

Vue.use(VueRouter)

// Prepare routes object
const routes: Array<RouteConfig> = []
for (let route of routesData.routes) {
  routes.push({
    path: route.path,
    component: () => import(`@/components/${route.component}.vue`)
  })
}

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
