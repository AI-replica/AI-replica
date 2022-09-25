import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";
import HomePage from "./HomePage/HomePage";
import TestPage from "./TestPage/TestPage";

// TODO: move route configuration into this file.
// Currenlty this configuration is not used.
const routes = [
    {
      path: "/",
      component: HomePage
    },
    {
      path: "/test",
      component: TestPage,
    }
];

