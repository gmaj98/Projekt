import { BrowserRouter, Routes, Route } from "react-router-dom";

import Articles from "./pages/Articles";
import Videos from "./pages/Videos";
import Navbar from "./components/Navbar";

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Articles />} />
        <Route path="/videos" element={<Videos />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
