import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { BrowserRouter } from 'react-router-dom';

const root = ReactDOM.createRoot(document.getElementById('root'));
// calling root.render() will instanciate the given components and render them
root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
