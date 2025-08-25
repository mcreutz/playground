# React Todo List - Vue vs React Comparison

This is an exact functional copy of the Vue.js todo app, but built with React. It demonstrates the differences between Vue.js and React frameworks while maintaining identical functionality.

## Key Differences from Vue Version

### State Management
- **Vue**: Uses `ref()` and `computed()` for reactive state
- **React**: Uses `useState()` and `useMemo()` for state management

### Dependency Injection
- **Vue**: Uses `provide()` and `inject()` for sharing state
- **React**: Uses React Context API with `createContext()` and `useContext()`

### Component Definition
- **Vue**: Single File Components (`.vue`) with `<template>`, `<script setup>`, and `<style scoped>`
- **React**: TypeScript files (`.tsx`) with JSX returned from functions

### Routing
- **Vue**: Vue Router with `useRouter()` and `<router-view>`
- **React**: React Router with `useNavigate()` and `<Outlet>`

### Event Handling
- **Vue**: `@click="handler"` and `@submit.prevent="handler"`
- **React**: `onClick={handler}` and `onSubmit={handler}` with `e.preventDefault()`

### Two-way Binding
- **Vue**: `v-model="value"` for automatic two-way binding
- **React**: `value={state}` + `onChange={setter}` for controlled components

### Conditional Rendering
- **Vue**: `v-if="condition"` and `v-else`
- **React**: `{condition ? <Component /> : <OtherComponent />}`

### List Rendering
- **Vue**: `v-for="item in items" :key="item.id"`
- **React**: `{items.map(item => <Component key={item.id} />)}`

### Lifecycle
- **Vue**: `onMounted()` composable
- **React**: `useEffect()` hook

### CSS Styling
- **Vue**: Scoped styles within `.vue` files
- **React**: Separate `.css` files imported into components

## Installation & Setup

```bash
cd /path/to/react/todo_list
npm install
npm run dev
```


