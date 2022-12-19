import Basics from "./Basics";
import Clock from "./Clock";
import { Form, Toggle, WithParam } from "./Events";
import { Routes, Route } from 'react-router-dom';


export default function App() {
    return (
        <>
            {/* Components to render on all routes (eg. Navbar) go here */}
            <Routes>
                <Route path="/" element={<Basics />} />
                <Route path="/clock" element={<Clock />} />
                <Route path="/form" element={<Form />} />
                <Route path="/toggle" element={<Toggle />} />
                <Route path="/withparam" element={<WithParam />} />
            </Routes>
        </>);
}