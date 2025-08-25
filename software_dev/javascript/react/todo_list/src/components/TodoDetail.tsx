import React, { useState, useEffect, useMemo } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { useAuth, useTodos } from '../context'

const TodoDetail: React.FC = () => {
    const { id } = useParams<{ id: string }>()
    const [editText, setEditText] = useState('')
    const navigate = useNavigate()
    const auth = useAuth()
    const todos = useTodos()

    const todo = useMemo(() => {
        return todos.todos.find(t => t.id === parseInt(id || '0'))
    }, [todos.todos, id])

    useEffect(() => {
        if (!auth.currentUser) {
            navigate('/login')
            return
        }

        if (todo) {
            setEditText(todo.text)
        }
    }, [auth.currentUser, todo, navigate])

    const goBack = () => {
        navigate('/')
    }

    const saveTodo = (e: React.FormEvent) => {
        e.preventDefault()
        if (todo && editText.trim()) {
            todos.updateTodo(todo.id, { text: editText.trim() })
        }
    }

    const cancelEdit = () => {
        if (todo) {
            setEditText(todo.text)
        }
    }

    const deleteTodo = () => {
        if (todo) {
            todos.removeTodo(todo.id)
            navigate('/')
        }
    }

    return (
        <div>
            <div className="detail-header">
                <button onClick={goBack} className="btn btn-secondary">← Back to List</button>
                <h1>Todo Details</h1>
            </div>

            {todo ? (
                <div className="todo-detail">
                    <div className="card">
                        <div className="status">
                            <input
                                type="checkbox"
                                checked={todo.completed}
                                onChange={(e) => {
                                    todos.updateTodo(todo.id, { completed: e.target.checked })
                                }}
                            />
                            <span className={todo.completed ? 'completed' : ''}>
                                {todo.completed ? 'Completed' : 'Not completed'}
                            </span>
                        </div>
                    </div>

                    <div className="card">
                        <h3>Edit Todo</h3>
                        <form onSubmit={saveTodo}>
                            <input
                                value={editText}
                                onChange={(e) => setEditText(e.target.value)}
                                type="text"
                                placeholder="Todo text..."
                                required
                            />
                            <div className="button-group">
                                <button type="submit" className="btn btn-success">Save</button>
                                <button type="button" onClick={cancelEdit} className="btn btn-secondary">Cancel</button>
                            </div>
                        </form>
                    </div>

                    <div className="actions">
                        <button onClick={deleteTodo} className="btn btn-danger">Delete Todo</button>
                    </div>
                </div>
            ) : (
                <div className="not-found">
                    <h2>Todo not found</h2>
                    <button onClick={goBack} className="btn btn-primary">Go back to list</button>
                </div>
            )}
        </div>
    )
}

export default TodoDetail
