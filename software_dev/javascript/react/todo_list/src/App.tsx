import React, { useState, useMemo, useEffect } from 'react'
import { BrowserRouter as Router, Routes, Route, Outlet, useNavigate, useLocation } from 'react-router-dom'
import { AuthContext, TodoContext } from './context'
import { Todo, User } from './types'
import TodoList from './components/TodoList'
import TodoDetail from './components/TodoDetail'
import Login from './components/Login'
import './styles.css'

const users: User[] = [
    { id: 'one', name: 'one', password: 'one' },
    { id: 'two', name: 'two', password: 'two' }
]

let nextId = 4

function AppContent() {
    const [currentUser, setCurrentUser] = useState<User | null>(null)
    const [allTodos, setAllTodos] = useState<Todo[]>([
        { id: 1, text: 'Learn React routing', completed: false, userId: 'one' },
        { id: 2, text: 'Build a multi-page app', completed: true, userId: 'one' },
        { id: 3, text: 'Add navigation', completed: false, userId: 'two' }
    ])

    const navigate = useNavigate()
    const location = useLocation()

    const todos = useMemo(() =>
        allTodos.filter(todo => todo.userId === currentUser?.id),
        [allTodos, currentUser]
    )

    useEffect(() => {
        if (!currentUser && location.pathname !== '/login') {
            navigate('/login')
        }
    }, [currentUser, location.pathname, navigate])

    const addTodo = (text: string) => {
        if (!currentUser) return
        setAllTodos(prev => [...prev, {
            id: nextId++,
            text,
            completed: false,
            userId: currentUser.id
        }])
    }

    const removeTodo = (id: number) => {
        setAllTodos(prev => prev.filter(todo => todo.id !== id))
    }

    const updateTodo = (id: number, updates: Partial<Todo>) => {
        setAllTodos(prev => prev.map(todo =>
            todo.id === id ? { ...todo, ...updates } : todo
        ))
    }

    const login = (username: string, password: string) => {
        const user = users.find(u => u.id === username && u.password === password)
        if (user) {
            setCurrentUser(user)
            return true
        }
        return false
    }

    const logout = () => {
        setCurrentUser(null)
        navigate('/login')
    }

    const authValue = { currentUser, login, logout }
    const todoValue = { todos, addTodo, removeTodo, updateTodo }

    return (
        <AuthContext.Provider value={authValue}>
            <TodoContext.Provider value={todoValue}>
                <div className="app">
                    {currentUser && (
                        <div className="header">
                            <div className="user-info">
                                Welcome, {currentUser.name}!
                                <button onClick={logout} className="btn btn-secondary">Logout</button>
                            </div>
                        </div>
                    )}
                    <Outlet />
                </div>
            </TodoContext.Provider>
        </AuthContext.Provider>
    )
}

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<AppContent />}>
                    <Route index element={<TodoList />} />
                    <Route path="todo/:id" element={<TodoDetail />} />
                    <Route path="login" element={<Login />} />
                </Route>
            </Routes>
        </Router>
    )
}

export default App
