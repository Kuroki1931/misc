import React, { useContext } from 'react'
import { withCookies } from "react-cookie";
import { ApiContext}  from "../context/ApiContext";
import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import IconButton from '@material-ui/core/IconButton';
import InfoIcon from '@material-ui/icons/Info';

const useStyles = makeStyles((theme) => ({
    root: {
      display: 'flex',
      flexWrap: 'wrap',
      justifyContent: 'space-around',
      overflow: 'hidden',
      backgroundColor: theme.palette.background.paper,
    },

    icon: {
      color: 'rgba(255, 255, 255, 0.54)',
    },
  }));

const Main = () => {
    const classes = useStyles();
    const { memos, setSelectedMemo } = useContext(ApiContext);


    return (
        <div>
            <container className={classes.root}>
                <GridList cellHeight={380} className={classes.gridList}>
                    <GridListTile key="Subheader" cols={2} style={{ height: 'auto' }}>
                    </GridListTile>
                    {memos.map((tile) => (
                    <GridListTile key={tile.id}>
                        <img src={tile.img} alt={tile.title} />
                        <GridListTileBar
                        title={tile.title}
                        subtitle={<span>by Miyazaki Hayao</span>}
                        actionIcon={
                            <IconButton aria-label={`info about ${tile.title}`} className={classes.icon} onClick={()=>{setSelectedMemo(tile)}}>
                            <InfoIcon />
                            </IconButton>
                        }
                        />
                    </GridListTile>
                    ))}
                </GridList>
            </container>
            <hr style={{ borderWidth: '10px'}}/>
        </div>
    )
}

export default withCookies(Main)
