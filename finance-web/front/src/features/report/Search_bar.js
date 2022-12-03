import React, {useState} from 'react';
import Autocomplete from '@material-ui/lab/Autocomplete';
import { fade, makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import classes from "./Search_bar.module.css";
import {HashLink} from 'react-router-hash-link';

const useStyles = makeStyles((theme) => ({
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
    }, 
  }));

const Search_bar = ({company_list}) => {
    const styles = useStyles();
    const [inputValue, setInputValue] = useState('');

    var option = [];
    var company_name_id = {}
    for (var i in company_list) {
        option.push(String(company_list[i].company_number))
        company_name_id[company_list[i].company_number] = company_list[i].id
    }
    const options = option

    return (
        <div className={classes.search_bar_head}>
            <Autocomplete
                inputValue={inputValue}
                onInputChange={(event, newInputValue) => {
                setInputValue(newInputValue);
                }}
                id="controllable-states-demo"
                options={options}
                
                renderInput={(params) => <TextField {...params} label="Code"/>}
                classes={{
                    root: styles.inputRoot,
                    input: styles.inputInput,
                }}
                style={{'width': '200px'}}
                inputProps={{ 'aria-label': 'search' }}
                onKeyPress={e => {
                    if (e.key == 'Enter') {
                    e.preventDefault()
                    window.location.href = `/report/${company_name_id[inputValue]}/#piyo`
                }}}
            />   
        </div>
    )
}

export default Search_bar
