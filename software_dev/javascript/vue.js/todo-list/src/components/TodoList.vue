<template>
  <div>
    <h1>Todo List</h1>
    
    <!-- Add Todo -->
    <div class="add-section">
      <form @submit.prevent="addTodo">
        <input v-model="newTodo" placeholder="Add a new todo..." required />
        <button type="submit" class="btn btn-primary">Add</button>
      </form>
    </div>

    <!-- Todo List -->
    <div class="list-section">
      <div v-if="todos.todos.value.length === 0" class="empty-state">
        No todos yet. Add one above!
      </div>
      
      <div v-else class="todo-container">
        <div class="todo-header">
          <span>Completed</span>
          <span>Task</span>
          <span>Actions</span>
        </div>
        
        <div v-for="todo in todos.todos.value" :key="todo.id" class="todo-item" :class="{ completed: todo.completed }">
          <div class="todo-status">
            <input type="checkbox" v-model="todo.completed" />
          </div>
          <div class="todo-task" @click="goToDetail(todo.id)">
            {{ todo.text }}
          </div>
          <div class="todo-actions">
            <button @click="removeTodo(todo.id)" class="btn btn-danger">Delete</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, inject, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const todos = inject<any>('todos')!
const auth = inject<any>('auth')!
const newTodo = ref('')
const router = useRouter()

onMounted(() => {
  if (!auth.currentUser.value) {
    router.push('/login')
  }
})

const addTodo = () => {
  if (newTodo.value.trim()) {
    todos.addTodo(newTodo.value.trim())
    newTodo.value = ''
  }
}

const removeTodo = (id: number) => {
  todos.removeTodo(id)
}

const goToDetail = (id: number) => {
  router.push(`/todo/${id}`)
}
</script>

