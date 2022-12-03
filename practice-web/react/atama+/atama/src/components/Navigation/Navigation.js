import React, { useContext } from "react";
import Links from "./Links";
import classes from "./Navigation.module.css";
import { Link } from "react-router-dom";
import { CompanyContext } from "../../App";

function Navigation(props) {
  const { home, company, recruit } = useContext(CompanyContext);

  return (
    <div>
      <div
        onClick={props.click}
        className={classes.Container}
        style={{ padding: "30px 0", color: "#0095aa" }}
      >
        <nav>
          <Link className={classes.NavigateTitle} to="/company">
            Company
          </Link>
        </nav>
        {company.map((link, index) => (
          <Links title={link.title} url={link.url} key={index} />
        ))}
        <div>
          <div
            style={{
              padding: "10px 0 30px",
              borderBottom: "1px solid #dbeaec",
            }}
          >
            <p
              style={{
                fontSize: "12px",
              }}
            >
              東京都品川区西五反田4-31-18 目黒テクノビル2F
              <br /> Nishigotanda 4-31-18, Shinagawa-ku, Tokyo, Japan
            </p>

            <a className={classes.MoreInfo} href="https://service.atama.plus/">
              Service Site
            </a>
          </div>
          <div>
            <h3>Follow us</h3>
            <a
              href="https://www.facebook.com/atamaplus/"
              target="_blank"
              rel="noreferrer noopener"
              className={classes.iconFB}
            >
              　
            </a>
            <p style={{ fontSize: "10px" }}>
              © atama plus Inc. | Privacy Policy
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Navigation;
