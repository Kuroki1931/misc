import React from 'react'
import classes from './Navigation.module.css'

const Links = (props) => {
    return (
        <div>
            <a href={props.url} className={classes.Links}>
                {props.title}
            </a>
        </div>
    )
}

export default Links
