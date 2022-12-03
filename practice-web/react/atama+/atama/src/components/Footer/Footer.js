import Navigation from "../Navigation/Navigation";
import classes from "./Footer.module.css";
import React, { useContext } from "react";
import { NavLink } from "react-router-dom";
import { HomeContext, CompanyContext, RecruitContext } from "../../App";
import Links from "../Navigation/Links";
import logo from "../../assets/images/atama+.png";

function Footer() {
  const { home, company, recruit } = useContext(CompanyContext);
  // const company = useContext(CompanyContext);
  // const recruit = useContext(RecruitContext);
  return (
    <div className={classes.Footer}>
      <div className={classes.Navigate}>
        <Navigation />
      </div>
      <div className={classes.smallFoot}>
        <div className={classes.Foot}>
          <div className={classes.Tags}>
            <img src={logo} alt="ロゴ" />
            <p>
              東京都品川区西五反田4-31-18
              <br />
              目黒テクノビル2F
              <br />
              Nishigotanda 4-31-18,
              <br />
              Shinagawa-ku, Tokyo, Japan
            </p>
          </div>
        </div>

        <nav>
          <div className={classes.HeadNav}>
            <ul className={classes.Tags}>
              <li>
                <NavLink to="/Company" exact>
                  Company
                </NavLink>
                <ul className={classes.Tag}>
                  {company.map((link, index) => (
                    <li>
                      <Links title={link.title} url={link.url} key={index} />
                    </li>
                  ))}
                </ul>
              </li>
            </ul>
          </div>
        </nav>
      </div>
    </div>
  );
}
export default Footer;
