import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import Clock from './Clock';

const root = ReactDOM.createRoot(document.getElementById('root'));
// calling root.render() will instanciate the given components and render them
root.render(
  <React.StrictMode>
    <App />
    <Clock />
  </React.StrictMode>
);
