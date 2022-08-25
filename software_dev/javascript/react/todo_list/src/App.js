// Tutorial from https://www.youtube.com/watch?v=hQAHSlTtcmY

// 'useState' stores currrent state ???
// 'useRef' allows access to other components
// 'useEfffect' ???
import { useState, useRef, useEffect } from 'react';

import TodoList from './TodoList'  // import our own component
import uuidv4 from 'uuid/dist/v4'  // to create unique IDs for todos


const LOCAL_STORAGE_KEY = 'todoApp.todos'  // Key to reference our todos in 'useEffect'


function App() {
  const [todos, setTodos] = useState([])
  const todoNameRef = useRef()

  // On app load, get stored todos from storage. If not empty, load.
  // Content of '[]' is monitored for change to trigger this function. No ccontent means triggger on startup.
  useEffect(() => {
    const storedTodos = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY))
    if (storedTodos) setTodos(storedTodos)
  }, [])

  // Update local storage of todos, whenenver todos get modified.
  useEffect(() => {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(todos))
  }, [todos])


  // On toggle of chackbox, copy all todos, then toggle '.complete' of given 'id' and update.
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
