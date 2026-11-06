
import { BrowserRouter, Routes, Route } from "react-router-dom";

import MainLayout from "./layouts/MainLayout";
import Dashboard from "./pages/Dashboard";
import Customers from "./pages/Customers";
import Tickets from "./pages/Tickets";
import Conversations from "./pages/Conversations";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<MainLayout />}>
          <Route path="/" element={<Dashboard />} />
          <Route path="/customers" element={<Customers />} />
          <Route path="/tickets" element={<Tickets />} />
          <Route path="/conversations" element={<Conversations />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
