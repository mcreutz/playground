export interface Todo {
    id: number
    text: string
    completed: boolean
    userId: string
}

export interface User {
    id: string
    name: string
    password: string
}
