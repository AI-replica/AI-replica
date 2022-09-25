import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { BASE_ROUTER_URL } from './utils/constants';
import ROUTES from './utils/routes';

const root = ReactDOM.createRoot(document.getElementById('root')!);
root.render(
  <React.StrictMode>
    {
    // need to specify basename as the chat is served at '/chat` path
    // https://v5.reactrouter.com/web/api/BrowserRouter/basename-string
    }
    <BrowserRouter basename={BASE_ROUTER_URL}>
        {ROUTES}
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
