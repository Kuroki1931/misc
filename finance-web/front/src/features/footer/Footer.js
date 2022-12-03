import React, { useContext } from "react";
import logo from '../icon/logo.png';
import classes from './Footer.module.css';
import { FinanceContext } from "../../App";
import { Link } from 'react-router-dom';
import Button from '@material-ui/core/Button';

const Footer = () => {
    const { links_info } = useContext(FinanceContext);

    return (
        <div className={classes.all}>
            <footer className={classes.footer_box}>
                <div>
                    <img src={logo} className={classes.logo}/>
                </div>
                <div className={classes.each_box}>
                    <div className={classes.top_font}>ABOUT US</div>
                    {links_info.map((link) => (
                        <div>
                            <Link to={link.url} style={{textDecoration: 'none', color: 'black'}}>
                                <div className={classes.link_font}>
                                {link.title}
                                </div>
                            </Link>
                        </div>
                    ))} 
                </div>
                <div className={classes.each_box}>
                    <div className={classes.top_font}>CONTACT US</div>
                    <a href='https://docs.google.com/forms/d/e/1FAIpQLSfufDZ65-WX590zRFBDBF41EH0AD2Hk4LqPq_wbex7FAfepBA/viewform'　className={classes.link_font} style={{textDecoration: 'none', color: 'black'}}>こちらのformから</a>
                </div>
            </footer>
        </div>
    )
}

export default Footer
