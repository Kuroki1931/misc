import React, { createContext } from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App'
import Login from './components/Login'
import reportWebVitals from './reportWebVitals';
import { Route, BrowserRouter, Switch } from 'react-router-dom';
import { CookiesProvider } from 'react-cookie'

ReactDOM.render(
  <React.StrictMode>
      <BrowserRouter>
        <CookiesProvider>
          <Switch>
            <Route exact path='/' component={Login} />
            <Route exact path='/main' component={App} />
          </Switch>
        </CookiesProvider>
      </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
