import React from 'react';
import footer_logo from '../app_bar/東大金融研究会_ロゴ.png';
import classes from './Footer.module.css';

const Footer = () => {
    return (
        <div>
            <footer className={classes.footer_box}>
                <img src={footer_logo} className={classes.logo}/>
            </footer>
        </div>
    )
}

export default Footer
