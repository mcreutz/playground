import { createContext, useContext } from 'react'
import { Todo, User } from './types'

export interface AuthContextType {
    currentUser: User | null
    login: (username: string, password: string) => boolean
    logout: () => void
}

export interface TodoContextType {
    todos: Todo[]
    addTodo: (text: string) => void
    removeTodo: (id: number) => void
    updateTodo: (id: number, updates: Partial<Todo>) => void
}

export const AuthContext = createContext<AuthContextType | null>(null)
export const TodoContext = createContext<TodoContextType | null>(null)

export const useAuth = () => {
    const context = useContext(AuthContext)
    if (!context) {
        throw new Error('useAuth must be used within an AuthProvider')
    }
    return context
}

export const useTodos = () => {
    const context = useContext(TodoContext)
    if (!context) {
        throw new Error('useTodos must be used within a TodoProvider')
    }
    return context
}
