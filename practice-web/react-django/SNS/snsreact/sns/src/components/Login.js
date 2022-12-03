import React, { useState, useReducer } from 'react'
import { withCookies } from 'react-cookie'
import axios from 'axios'
import Main from './Main'
import { Switch } from 'react-router-dom'
import {
    START_FETCH,
    FETCH_SUCCESS,
    ERROR_CATCHED,
    INPUT_EDIT,
    TOGGLE_MODE,
  } from "./actionTypes";

const initialState = {
    isLoading: false,
    isLoginView: true,
    error: "",
    credentialsLog: {
      username: "",
      password: "",
    },
    credentialsReg: {
      email: "",
      password: "",
    },
  };
  
  const loginReducer = (state, action) => {
    switch (action.type) {
      case START_FETCH: {
        return {
          ...state,
          isLoading: true,
        };
      }
      case FETCH_SUCCESS: {
        return {
          ...state,
          isLoading: false,
        };
      }
      case ERROR_CATCHED: {
        return {
          ...state,
          error: "Email or password is not correct!",
          isLoading: false,
        };
      }
      case INPUT_EDIT: {
        return {
          ...state,
          [action.inputName]: action.payload,
          error: "",
        };
      }
      case TOGGLE_MODE: {
        return {
          ...state,
          isLoginView: !state.isLoginView,
        };
      }
      default:
        return state;
    }
  };
  
  const Login = (props) => {
    const [state, dispatch] = useReducer(loginReducer, initialState);
  
    const inputChangedLog = () => (event) => {
      const cred = state.credentialsLog;
      cred[event.target.name] = event.target.value;
      dispatch({
        type: INPUT_EDIT,
        inputName: "state.credentialLog",
        payload: cred,
      });
    };
  
    const inputChangedReg = () => (event) => {
      const cred = state.credentialsReg;
      cred[event.target.name] = event.target.value;
      dispatch({
        type: INPUT_EDIT,
        inputName: "state.credentialReg",
        payload: cred,
      });
    };
  
    const login = async (event) => {
      event.preventDefault();
      if (state.isLoginView) {
        try {
          dispatch({ type: START_FETCH });
          const res = await axios.post(
            "http://127.0.0.1:8000/authen/",
            state.credentialsLog,
            {
              headers: { "Content-Type": "application/json" },
            }
          );
          props.cookies.set("current-token", res.data.token);
          res.data.token
            ? (window.location.href = "/main")
            : (window.location.href = "/");
          dispatch({ type: FETCH_SUCCESS });
        } catch {
          dispatch({ type: ERROR_CATCHED });
        }
      } else {
        try {
          dispatch({ type: START_FETCH });
          await axios.post(
            "http://127.0.0.1:8000/user/create/",
            state.credentialsReg,
            {
              headers: { "Content-Type": "application/json" },
            }
          );
          dispatch({ type: FETCH_SUCCESS });
          dispatch({ type: TOGGLE_MODE });
        } catch {
          dispatch({ type: ERROR_CATCHED });
        }
      }
    };
  
    const toggleView = () => {
      dispatch({ type: TOGGLE_MODE });
    };
  
    return (
        <form onSubmit={login}>
          <div>
            <div>
              {state.isLoginView ? "Login" : "Register"}
            </div>
           
            <div>Email</div>
            {state.isLoginView ? (
              <input
                name="username"
                value={state.credentialsLog.username}
                onChange={inputChangedLog()}
              />
            ) : (
              <input
                name="email"
                value={state.credentialsReg.email}
                onChange={inputChangedReg()}
              />
            )}

            <br/>
           
            <div>password</div>
            {state.isLoginView ? (
              <input
                name="password"
                value={state.credentialsLog.password}
                onChange={inputChangedLog()}
              />
            ) : (
              <input
                name="password"
                value={state.credentialsReg.password}
                onChange={inputChangedReg()}
              />
            )}
            <span>{state.error}</span>

            <br/>
  
            {state.isLoginView ? (
              !state.credentialsLog.password || !state.credentialsLog.username ? (
                <button
                  type="submit"
                  disabled
                >
                  Login
                </button>
              ) : (
                <button
                  type="submit"
                >
                  Login
                </button>
              )
            ) : !state.credentialsReg.password || !state.credentialsReg.email ? (
              <button
                type="submit"
                disabled
              >
                Register
              </button>
            ) : (
              <button
                type="submit"
              >
                Register
              </button>
            )}

            <br/>

            <button onClick={() => toggleView()}>
              {state.isLoginView ? "Create Accout ?" : "Back to login ?"}
            </button>
          </div>
        </form>
    );
  };
  
  export default withCookies(Login);
  