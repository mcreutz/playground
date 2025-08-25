<template>
  <div class="app">
    <div v-if="currentUser" class="header">
      <div class="user-info">
        Welcome, {{ currentUser.name }}!
        <button @click="logout" class="btn btn-secondary">Logout</button>
      </div>
    </div>
    <router-view />
  </div>
</template>

<script setup lang="ts">
import { ref, provide, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import type { Todo, User } from './types'

const router = useRouter()

const users: User[] = [
  { id: 'one', name: 'one', password: 'one' },
  { id: 'two', name: 'two', password: 'two' }
]

const currentUser = ref<User | null>(null)
const allTodos = ref<Todo[]>([
  { id: 1, text: 'Learn Vue.js routing', completed: false, userId: 'one' },
  { id: 2, text: 'Build a multi-page app', completed: true, userId: 'one' },
  { id: 3, text: 'Add navigation', completed: false, userId: 'two' }
])

let nextId = 4

const todos = computed(() => 
  allTodos.value.filter(todo => todo.userId === currentUser.value?.id)
)

onMounted(() => {
  if (!currentUser.value && router.currentRoute.value.path !== '/login') {
    router.push('/login')
  }
})

const addTodo = (text: string) => {
  if (!currentUser.value) return
  allTodos.value.push({
    id: nextId++,
    text,
    completed: false,
    userId: currentUser.value.id
  })
}

const removeTodo = (id: number) => {
  allTodos.value = allTodos.value.filter(todo => todo.id !== id)
}

const login = (username: string, password: string) => {
  const user = users.find(u => u.id === username && u.password === password)
  if (user) {
    currentUser.value = user
    return true
  }
  return false
}

const logout = () => {
  currentUser.value = null
  router.push('/login')
}

provide('auth', { currentUser, login, logout })
provide('todos', { todos, addTodo, removeTodo })
</script>

