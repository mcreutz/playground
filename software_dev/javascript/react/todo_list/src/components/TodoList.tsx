import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth, useTodos } from '../context'

const TodoList: React.FC = () => {
    const [newTodo, setNewTodo] = useState('')
    const navigate = useNavigate()
    const auth = useAuth()
    const todos = useTodos()

    useEffect(() => {
        if (!auth.currentUser) {
            navigate('/login')
        }
    }, [auth.currentUser, navigate])

    const addTodo = (e: React.FormEvent) => {
        e.preventDefault()
        if (newTodo.trim()) {
            todos.addTodo(newTodo.trim())
            setNewTodo('')
        }
    }

    const removeTodo = (id: number) => {
        todos.removeTodo(id)
    }

    const goToDetail = (id: number) => {
        navigate(`/todo/${id}`)
    }

    return (
        <div>
            <h1>Todo List</h1>

            {/* Add Todo */}
            <div className="add-section">
                <form onSubmit={addTodo}>
                    <input
                        value={newTodo}
                        onChange={(e) => setNewTodo(e.target.value)}
                        placeholder="Add a new todo..."
                        required
                    />
                    <button type="submit" className="btn btn-primary">Add</button>
                </form>
            </div>

            {/* Todo List */}
            <div className="list-section">
                {todos.todos.length === 0 ? (
                    <div className="empty-state">
                        No todos yet. Add one above!
                    </div>
                ) : (
                    <div className="todo-container">
                        <div className="todo-header">
                            <span>Completed</span>
                            <span>Task</span>
                            <span>Actions</span>
                        </div>

                        {todos.todos.map(todo => (
                            <div
                                key={todo.id}
                                className={`todo-item ${todo.completed ? 'completed' : ''}`}
                            >
                                <div className="todo-status">
                                    <input
                                        type="checkbox"
                                        checked={todo.completed}
                                        onChange={(e) => {
                                            todos.updateTodo(todo.id, { completed: e.target.checked })
                                        }}
                                    />
                                </div>
                                <div className="todo-task" onClick={() => goToDetail(todo.id)}>
                                    {todo.text}
                                </div>
                                <div className="todo-actions">
                                    <button onClick={() => removeTodo(todo.id)} className="btn btn-danger">
                                        Delete
                                    </button>
                                </div>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    )
}

export default TodoList
