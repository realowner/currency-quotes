import React from "react";
import Header from "./components/Header";
import Quotes from "./components/Quotes";
import './styles/App.css';

function App() {
  return (
    <div className="App">
      <Header/>
      <Quotes/>
    </div>
  );
}

export default App;