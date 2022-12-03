import React from 'react'
import classes from './Navbar.module.css'
import { withCookies } from 'react-cookie'

const Navbar = (props) => {
    const Logout = () => event => {
        props.cookies.remove('current-token');
        window.location.href = '/';

    }


    return (
        <div>
            <container>
                <img 
                src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/1200px-Instagram_logo_2016.svg.png'
                alt='no-image'
                style={{ width:'2%' }}
                className={classes.inline}
                />
                <h3 
                  className={classes.inline}
                  style={{ margin:'0 0 0 35vw' }}
                >
                    Kuroki's SNS
                </h3>
                <button 
                  className={classes.inline}
                  style={{ margin:'0 0 0 35vw' }}
                  onClick={Logout()}>Logout</button>
            </container>
            
        </div>
    )
}

export default withCookies(Navbar)
