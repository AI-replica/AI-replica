import {
  Routes,
  Route,
} from "react-router-dom";
import App from "../App/App";
import HomePage from "../HomePage/HomePage";
import TestPage from "../TestPage/TestPage";

const ROUTES = (
    <Routes>
        <Route path="/" element={<App />}>
            <Route path="/" element={<HomePage />} />
            <Route path="index.html" element={<HomePage />} />
            <Route path="/test" element={<TestPage />} />
        </Route>      
    </Routes>
)

export default ROUTES;
