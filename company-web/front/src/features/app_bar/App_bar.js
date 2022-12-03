import React, {useState} from 'react';
import { fade, makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import SearchIcon from '@material-ui/icons/Search';
import header_logo from './東大金融研究会_ロゴ.png';
import styles from './app_bar.module.css';
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';
import { useSelector, useDispatch } from "react-redux";

import {
  selectCompany_list
} from "../company/companySlice";

const useStyles = makeStyles((theme) => ({
  grow: {
    flexGrow: 1,
  },
  menuButton: {
    display: 'none',
    [theme.breakpoints.up('sm')]: {
      display: 'block',
      marginRight: theme.spacing(1),
    },
  },
  
  title: {
    display: 'none',
    [theme.breakpoints.up('sm')]: {
      display: 'block',
    },
  },
  search: {
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    backgroundColor: fade(theme.palette.common.white, 0.15),
    '&:hover': {
      backgroundColor: fade(theme.palette.common.white, 0.25),
    },
    marginRight: theme.spacing(2),
    marginLeft: 0,
    width: '80%',
    [theme.breakpoints.up('sm')]: {
      marginLeft: theme.spacing(3),
      width: 'auto',
    },
  },
  searchIcon: {
    padding: theme.spacing(0, 2),
    height: '100%',
    position: 'absolute',
    pointerEvents: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  inputRoot: {
    color: 'inherit',
  },
  inputInput: {
    padding: theme.spacing(1, 1, 1, 0),
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
    transition: theme.transitions.create('width'),
    width: '100%',
    [theme.breakpoints.up('md')]: {
      width: '20ch',
    },
    color: '#fff',
  }, 
}));

export default function PrimarySearchAppBar() {
  const classes = useStyles();
  const search_company = useSelector(selectCompany_list);
  const [inputValue, setInputValue] = useState('');
  const [value, setValue] = useState(["name"]);

  var option = [];
  var company_id = {}
  for (var i in search_company) {
      option.push(search_company[i].name)
      company_id[search_company[i].name] = search_company[i].id
  }
  const options = option

  return (
    <div>
      <AppBar position="static" style={{ backgroundColor: "black" }}>
        <Toolbar>
          <IconButton
            edge="start"
            className={classes.menuButton}
            color="inherit"
            aria-label="open drawer"
          >
            <img src={header_logo} className={styles.logo}/>
          </IconButton>
          <div className={classes.search}>
            <div className={classes.searchIcon}>
              <SearchIcon/>
            </div>
            <Autocomplete
              value={value}
              inputValue={inputValue}
              onInputChange={(event, newInputValue) => {
              setInputValue(newInputValue);
              }}
              id="controllable-states-demo"
              options={options}
              style={{ width: 200, paddingLeft: 50}}
              renderInput={(params) => <TextField {...params}/>}
              classes={{
                root: classes.inputRoot,
                input: classes.inputInput,
              }}
              inputProps={{ 'aria-label': 'search' }}
              onKeyPress={e => {
                if (e.key == 'Enter') {
                  e.preventDefault()
                  window.location.href = `/company/${company_id[inputValue]}/`
              }}}
            
            />   
          </div>
          <div className={classes.grow} />
        </Toolbar>
      </AppBar>
    </div>
  );
}