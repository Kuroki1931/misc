import React from "react";
import Navigation from "./Navigation";
import classes from "./NavigationWindow.module.css";

function NavigationWindow(props) {
  return (
    <div className={classes.Window}>
      <Navigation click={props.click} />
    </div>
  );
}

export default NavigationWindow;
