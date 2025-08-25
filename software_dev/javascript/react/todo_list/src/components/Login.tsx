import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../context'

const Login: React.FC = () => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [errorMessage, setErrorMessage] = useState('')
    const navigate = useNavigate()
    const auth = useAuth()

    const handleLogin = (e: React.FormEvent) => {
        e.preventDefault()
        setErrorMessage('')

        if (auth.login(username, password)) {
            navigate('/')
        } else {
            setErrorMessage('Invalid username or password')
            setPassword('')
        }
    }

    return (
        <div className="login-container">
            <div className="login-form">
                <h1>Todo App Login</h1>

                <form onSubmit={handleLogin}>
                    <div className="form-group">
                        <label htmlFor="username">Username</label>
                        <input
                            id="username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            placeholder="Enter username"
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="password">Password</label>
                        <input
                            id="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            type="password"
                            placeholder="Enter password"
                            required
                        />
                    </div>

                    <button type="submit" className="btn btn-primary">Login</button>

                    {errorMessage && (
                        <div className="error-message">
                            {errorMessage}
                        </div>
                    )}
                </form>

                <div className="demo-info">
                    <p><strong>Demo users:</strong></p>
                    <p>Username: <code>one</code> | Password: <code>one</code></p>
                    <p>Username: <code>two</code> | Password: <code>two</code></p>
                </div>
            </div>
        </div>
    )
}

export default Login
