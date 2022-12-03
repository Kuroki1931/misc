import React from 'react';
import { withCookies } from 'react-cookie'
import { makeStyles } from '@material-ui/core/styles';
import TagFacesIcon from '@material-ui/icons/TagFaces';
import KeyboardBackspaceIcon from '@material-ui/icons/KeyboardBackspace';

const useStyles = makeStyles((theme) => ({
    dis: {
        display: 'flex',
        padding: theme.spacing(2),
        backgroundColor: '#0000FF',
    },
}));

const Header = (props) => {
    const classes = useStyles();
    const Logout = () => event => {
        props.cookies.remove('current-token');
        window.location.href='/';
    }

    return (
        <div className={classes.dis}>
            <span style={{ padding: '0 10% 0 10%' }}>
                <TagFacesIcon/>
            </span>
            <span style={{ fontWeight: "bold", margin: '0 24% 0 24%', fontSize: '20px'}}>
                <span>ジブリ</span>
            </span>
            <button style={{ margin: '0 10% 0 10%', background: 'transparent', border: 'none'}} onClick={Logout()}>
                <KeyboardBackspaceIcon/>
            </button>
        </div>
    )
}

export default withCookies(Header)
