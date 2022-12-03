import React from "react";
import './App.css';
import Main from './components/Main';
import Navbar from './components/Navbar';
import ApiContextProvider from "./context/ApiContext";

function App() {
  return (
    <div>
      <ApiContextProvider>
        <Navbar />
        <Main />
      </ApiContextProvider>
    </div>
  );
}


export default App;
