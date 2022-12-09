import React from 'react';
import ReactDOM from 'react-dom/client';
import Basics from './Basics';
import Clock from './Clock';
import { Form, Toggle, WithParam } from './Events';


const root = ReactDOM.createRoot(document.getElementById('root'));
// calling root.render() will instanciate the given components and render them
root.render(
  <React.StrictMode>
    <Basics />
    <Clock />
    <Form />
    <Toggle />
    <br></br>
    <WithParam />
  </React.StrictMode>
);
