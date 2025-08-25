import { createRouter, createWebHistory } from 'vue-router'
import TodoList from './components/TodoList.vue'
import TodoDetail from './components/TodoDetail.vue'
import Login from './components/Login.vue'

const routes = [
  { path: '/login', component: Login },
  { path: '/', component: TodoList },
  { path: '/todo/:id', component: TodoDetail, props: true }
]

export default createRouter({
  history: createWebHistory(),
  routes
})