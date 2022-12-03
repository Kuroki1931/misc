import './App.css';
import Company from './components/Company/Company';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import { createContext } from 'react';
import Header from './components/header/Header';
import Footer from './components/Footer/Footer';

export const CompanyContext = createContext()

function App() {

  const company = [
    {
      title: 'Mission',
      url: '/Company/#topMission',
    },
    {
      title: 'Members',
      url: '/Company/#topMembers',
    },
    {
      title: 'Corporate info',
      url: '/Company/#corporate',
    },
  ]


  return (
    <div className="App">
      <BrowserRouter >
        <CompanyContext.Provider value={{company}}>
          <Header />
          <Switch>
           <Route path="/company/" component={Company} exact />
          </Switch>
          <Footer />
        </CompanyContext.Provider>
      </BrowserRouter>
    </div>
  );
}

export default App;
