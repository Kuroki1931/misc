import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import './App.css';
import App_bar from './features/app_bar/App_bar';
import Footer from './features/footer/Footer';
import How_read from './features/how_read/How_read';
import Our_company from './features/our_company/Our_company';
import Payment from './features/payment/Payment';
import Register from './features/register/Register';
import Report from './features/report/Report';
import Login from './features/login/Login';
import {Elements} from '@stripe/react-stripe-js';
import {loadStripe} from "@stripe/stripe-js/pure";
import { createContext } from 'react';

const PK_TEST = process.env.REACT_APP_PK_TEST
const stripePromise = loadStripe(String(PK_TEST));
export const FinanceContext = createContext(PK_TEST)

function App() {
  const links_info = [
    {
      title: '企業レポート',
      url: '/report/',
    },
    {
      title: '読み方',
      url: '/how_read/',
    },
    {
      title: '東大金融会とは',
      url: '/',
    },
    {
      title: 'ログイン',
      url: '/login/',
    },
    {
      title: '会員登録',
      url: '/register/',
    },
  ]
  return (
    <div className="App">
        <Router>
          <FinanceContext.Provider value={{links_info}}>
            <App_bar />
            <Route exact path='/how_read/' component={How_read}/>
            <Route exact path='/' component={Our_company}/>
            <Route exact path='/report/*/' component={Report}/>
            <Route exact path='/login/' component={Login}/>
            <Route exact path='/register/' component={Register}/>
            <Elements stripe={stripePromise}>
                <Route exact path='/register/payment/' component={Payment}/>
            </Elements>
            <Footer />
          </FinanceContext.Provider>
        </Router>
    </div>
  );
}

export default App;
