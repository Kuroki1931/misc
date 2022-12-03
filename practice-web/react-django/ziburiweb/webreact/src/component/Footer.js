import React from 'react';
import { withCookies } from 'react-cookie'
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
    dis: {
        padding: theme.spacing(2),
        backgroundColor: '#0000FF',
        textAlign: 'center',
        fontWeight: 'bold',
    },
}));

const Footer = (props) => {
    const classes = useStyles();

    return (
        <div className={classes.dis}>
            What do you watch next?
        </div>
    )
}

export default withCookies(Footer)
