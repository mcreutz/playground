<template>
  <div>
    <div class="detail-header">
      <button @click="goBack" class="btn btn-secondary">← Back to List</button>
      <h1>Todo Details</h1>
    </div>

    <div v-if="todo" class="todo-detail">
      <div class="card">
        <div class="status">
          <input
            type="checkbox"
            v-model="todo.completed"
          />
          <span :class="{ completed: todo.completed }">
            {{ todo.completed ? 'Completed' : 'Not completed' }}
          </span>
        </div>
      </div>

      <div class="card">
        <h3>Edit Todo</h3>
        <form @submit.prevent="saveTodo">
          <input
            v-model="editText"
            type="text"
            placeholder="Todo text..."
            required
          />
          <div class="button-group">
            <button type="submit" class="btn btn-success">Save</button>
            <button type="button" @click="cancelEdit" class="btn btn-secondary">Cancel</button>
          </div>
        </form>
      </div>

      <div class="actions">
        <button @click="deleteTodo" class="btn btn-danger">Delete Todo</button>
      </div>
    </div>

    <div v-else class="not-found">
      <h2>Todo not found</h2>
      <button @click="goBack" class="btn btn-primary">Go back to list</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, inject, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import type { Todo } from '../types'

const props = defineProps<{
  id: string
}>()

const todos = inject<any>('todos')!
const auth = inject<any>('auth')!
const router = useRouter()
const editText = ref('')

const todo = computed(() => {
  return todos.todos.value.find((t: Todo) => t.id === parseInt(props.id))
})

onMounted(() => {
  if (!auth.currentUser.value) {
    router.push('/login')
    return
  }
  
  if (todo.value) {
    editText.value = todo.value.text
  }
})

const goBack = () => {
  router.push('/')
}

const saveTodo = () => {
  if (todo.value && editText.value.trim()) {
    todo.value.text = editText.value.trim()
  }
}

const cancelEdit = () => {
  if (todo.value) {
    editText.value = todo.value.text
  }
}

const deleteTodo = () => {
  if (todo.value) {
    todos.removeTodo(todo.value.id)
    router.push('/')
  }
}
</script>

