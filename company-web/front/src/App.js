import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import './App.css';
import Company from './features/company/Company';
import Search from './features/search/Search';
import Property from './features/property/Property';
import Intern from './features/intern/Intern';



function App() {
  return (
    <div className="App">
      <Router>
        <Route exact path='/' component={Intern}/>
        <Route exact path='/search/*/' component={Search}/>
        <Route exact path='/company/*/' component={Company}/>
        <Route exact path='/property/*/' component={Property}/>
      </Router>
    </div>
  );
}

export default App;
