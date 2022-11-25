import React from "react";
import ChatUI from "./pages/Landing";
import Front from "./pages/Front";
import Recommendataion from "./pages/Recommendation";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import NavLayout from "./components/NavLayout/NavLayout";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<NavLayout />}>
          <Route index element={<Front />} />
          <Route path="/chat" element={<ChatUI />} />
          <Route path="/recommendations" element={<Recommendataion />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default App;
