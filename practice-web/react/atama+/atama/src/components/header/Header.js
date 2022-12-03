import React, { useState, useContext } from "react";
import NavigationWindow from "../Navigation/NavigationWindow";
import classes from "./Header.module.css";
import { NavLink } from "react-router-dom";
import { CompanyContext } from "../../App";
import Links from "../Navigation/Links";

const Header = () => {
  const { home, company, recruit } = useContext(CompanyContext);
  // const company = useContext(CompanyContext);
  // const recruit = useContext(RecruitContext);

  const [open, setOpen] = useState(false);
  let attachedClasses = [classes.Close];
  var scrollTop1 = 0;
  var scrollLeft1 = 0;
  const scrollPosition = () => {
    scrollTop1 = document.documentElement.scrollTop;
    scrollLeft1 = document.documentElement.scrollTop;
  };
  if (open) {
    scrollPosition();
    attachedClasses = [classes.Open];
    window.scrollTo(0, 0);
  }
  let attachedClasses1 = [classes.Icon, "fas fa-bars fa-3x"];
  if (open) {
    attachedClasses1 = [classes.Icon, "fas fa-times fa-3x"];
    window.scrollTo(scrollLeft1, scrollTop1);
  }
  const toggleHandler = () => {
    setOpen(!open);
  };

  return (
    <div>
      <div className={classes.Header}>
        <i
          onClick={() => toggleHandler()}
          className={attachedClasses1.join(" ")}
        ></i>
        <a href="/" className={classes.Logo}>
          　
        </a>
        <nav>
          <div className={classes.HeadNav}>
            <ul className={classes.Tags}>
              <li>
                <NavLink activeStyle={{ color: "#0095aa" }} to="/Company" exact>
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

      <div className={attachedClasses}>
        <NavigationWindow click={() => toggleHandler()} />
      </div>
    </div>
  );
};

export default Header;
