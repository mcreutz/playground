<template>
  <div class="login-container">
    <div class="login-form">
      <h1>Todo App Login</h1>
      
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="username">Username</label>
          <input id="username" v-model="username" placeholder="Enter username" required />
        </div>
        
        <div class="form-group">
          <label for="password">Password</label>
          <input id="password" v-model="password" type="password" placeholder="Enter password" required />
        </div>
        
        <button type="submit" class="btn btn-primary">Login</button>
        
        <div v-if="errorMessage" class="error-message">
          {{ errorMessage }}
        </div>
      </form>
      
      <div class="demo-info">
        <p><strong>Demo users:</strong></p>
        <p>Username: <code>one</code> | Password: <code>one</code></p>
        <p>Username: <code>two</code> | Password: <code>two</code></p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, inject } from 'vue'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const errorMessage = ref('')
const router = useRouter()
const auth = inject<any>('auth')!

const handleLogin = () => {
  errorMessage.value = ''
  
  if (auth.login(username.value, password.value)) {
    router.push('/')
  } else {
    errorMessage.value = 'Invalid username or password'
    password.value = ''
  }
}
</script>
