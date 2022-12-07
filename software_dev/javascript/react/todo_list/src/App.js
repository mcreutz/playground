// Tutorial from https://www.youtube.com/watch?v=hQAHSlTtcmY

import { useState, useRef, useEffect } from 'react';  // React hooks

import TodoList from './TodoList'  // import our own component
import uuidv4 from 'uuid/dist/v4'  // to create unique IDs for todos


const LOCAL_STORAGE_KEY = 'todoApp.todos'  // Key to reference our todos in 'useEffect', could be anything.


function App() {
  const [todos, setTodos] = useState([])  // 'useState' stores currrent state, changes of state re-renders the app
  const todoNameRef = useRef()  // 'useRef' allows access to other components by reference

  // On app load, get stored todos from storage. If not empty, load.
  // 'useEffect' monitors content of '[]' for change, then triggers this function. No content means triggger on startup.
  useEffect(() => {
    const storedTodos = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY))
    if (storedTodos) setTodos(storedTodos)
  }, [])

  // Update local storage of todos, whenenver todos get modified.
  useEffect(() => {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(todos))
  }, [todos])


  // On toggle of checkbox, copy all todos, then toggle '.complete' of given 'id' and update.
  function toggleTodo(id) {
    const newTodos = [...todos]
    const todo = newTodos.find(todo => todo.id === id)
    todo.complete = !todo.complete
    setTodos(newTodos)
  }

  // On add button click, get input text and add to todos. Then clear input.
  function handleAddTodo(e) {
    const name = todoNameRef.current.value
    if (name === '') return
    setTodos(prevTodos => {
      return [...prevTodos, { id: uuidv4(), name: name, complete: false }]
    })
    todoNameRef.current.value = null
  }

  // On clear button click, filter all todos with .complete false, then update.
  function handleClearTodos() {
    const newTodos = todos.filter(todo => !todo.complete)
    setTodos(newTodos)
  }


  return (
    // Encapsulate in empty tag, because 'return' can return only 1 object
    <>
      <TodoList todos={todos} toggleTodo={toggleTodo} />
      <input ref={todoNameRef} type="text" />  {/* ref to be readable from other component */}
      <button onClick={handleAddTodo}>Add todo</button>
      <button onClick={handleClearTodos}>Clear completed</button>
      <div>There are {todos.filter(todo => !todo.complete).length} todos left</div>
    </>
  )
}

export default App;
