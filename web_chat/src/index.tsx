import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App/App';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import TestPage from './TestPage/TestPage';
import { BASE_ROUTER_URL } from './utils/constants';

const root = ReactDOM.createRoot(document.getElementById('root')!);
// TODO: render content within App but not instead of App. App is a parent element to all pages.
root.render(
  <React.StrictMode>
    {/* <App /> */}
    {
    // need to specify basename as the chat is served at '/chat` path
    // https://v5.reactrouter.com/web/api/BrowserRouter/basename-string
    }
    <BrowserRouter basename={BASE_ROUTER_URL}>
        <Routes>
            <Route path="/index.html" element={<App />} />
            <Route path="/" element={<App />} />
            <Route path="/test" element={<TestPage />} />
        </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
