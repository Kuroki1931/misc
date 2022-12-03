import React, {useState} from "react";
import Button from "@material-ui/core/Button";
import { useSelector, useDispatch } from "react-redux";
import { withCookies } from 'react-cookie';
import styles from "./Login.module.css";

import {
  editEmail,
  editPassword,
  toggleMode,
  fetchAsyncLogin,
  fetchAsyncRegister,
  selectAuthen,
  selectIsLoginView,
} from "./loginSlice";

const ENDPOINT = process.env.REACT_APP_ENDPOINT
const apiUrl = String(ENDPOINT);

const Login = (props) => {
    const dispatch = useDispatch();
    const authen = useSelector(selectAuthen);
    const isLoginView = useSelector(selectIsLoginView);
    const btnDisabler1 = authen.email === "" || authen.password === "";
    const [error, setError] = useState('')


    const login = async () => {
        if (isLoginView) {
            const result = await dispatch(fetchAsyncLogin(authen))

            if (fetchAsyncLogin.fulfilled.match(result)) {
                props.cookies.set("current-token", result.payload.access, {maxAge: 3600, path: '/'});
                setError('')
            } else {
                setError('ログイン情報が間違っています')
            }
        } else {
            // const result = await dispatch(fetchAsyncRegister(authen));

            // if (fetchAsyncRegister.fulfilled.match(result)) {
            //     const result = await dispatch(fetchAsyncLogin(authen))
            // }
            // if (fetchAsyncLogin.fulfilled.match(result)) {
            //     props.cookies.set("current-token", result.payload.access, {maxAge: 3600, path: '/'});
            // }
        }
    };

    return (
        <div className={styles.containerLogin}>
            <div className={styles.appLogin}>
                <h1>{isLoginView ? "Login" : "Register"}</h1>
                <span>Email</span>
                <input
                    type="text"
                    className={styles.inputLog}
                    name="username"
                    placeholder=""
                    onChange={(e) => dispatch(editEmail(e.target.value))}
                    required
                />
                <span>Password</span>
                <input
                    type="password"
                    className={styles.inputLog}
                    name="password"
                    placeholder=""
                    onChange={(e) => dispatch(editPassword(e.target.value))}
                    required
                />
                <div style={{color: 'red'}}>{error}</div>
                <a href={`${apiUrl}accounts/password_reset_form/`} className={styles.forget_pas}>Forget password</a>
                <div className={styles.switch}>
                <Button
                    variant="contained"
                    disabled={btnDisabler1}
                    color="primary"
                    onClick={login}
                >
                    {isLoginView ? "Login" : "Create"}
                </Button>
                </div>
                {/* <span
                className={styles.switchText}
                onClick={() => dispatch(toggleMode())}
                >
                {isLoginView ? "Create Account ?" : "Back to Login"}
                </span> */}
            </div>
        </div>
    );
};

export default withCookies(Login)
