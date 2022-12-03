import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

const ENDPOINT = process.env.REACT_APP_ENDPOINT
const apiUrl = String(ENDPOINT);

export const fetchAsyncLogin = createAsyncThunk("login/post", async (auth) => {
  const res = await axios.post(`${apiUrl}authen/jwt/create`, auth, {
    headers: {
      "Content-Type": "application/json",
    },
  });
  return res.data;
});

export const fetchAsyncRegister = createAsyncThunk(
  "create/post",
  async (auth) => {
    const createData = new FormData();
    createData.append('Email', auth.email)
    createData.append('password', auth.password)
    createData.append('Username', 'all')
    const res = await axios.post(`${apiUrl}api/create/`, auth, {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return res.data;
  }
);

const loginSlice = createSlice({
  name: "login",
  initialState: {
    authen: {
      email: "",
      password: "",
    },
    isLoginView: true,
  },
  reducers: {
    editEmail(state, action) {
      state.authen.email = action.payload;
    },
    editPassword(state, action) {
      state.authen.password = action.payload;
    },
    toggleMode(state) {
      state.isLoginView = !state.isLoginView;
    },
  },
  extraReducers: (builder) => {
    builder.addCase(fetchAsyncLogin.fulfilled, (state, action) => {
      action.payload.access && (window.location.href = "/report/");
    });
  },
});
export const { editEmail, editPassword, toggleMode } = loginSlice.actions;
export const selectAuthen = (state) => state.login.authen;
export const selectIsLoginView = (state) => state.login.isLoginView;

export default loginSlice.reducer;
