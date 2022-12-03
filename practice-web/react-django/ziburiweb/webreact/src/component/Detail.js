import React, { useContext } from 'react'
import { withCookies } from "react-cookie";
import { ApiContext}  from "../context/ApiContext";
import DeleteIcon from '@material-ui/icons/Delete';

const Detail = () => {
    const { selectedMemo, deleteMemo } = useContext(ApiContext);

    return (
        <div>
            <h1>詳細</h1>
            <dl>
                <dt>title</dt>
                <dd>{ selectedMemo.title }</dd>
                <dt>memo</dt>
                <dd>{ selectedMemo.memo }</dd>
                <dt>写真</dt>
                <dd><img src={ selectedMemo.img } style={{ width: '50%'}}/></dd>
            </dl>
            <DeleteIcon onClick={()=>{deleteMemo()}}/>
        </div>
    )
}

export default withCookies(Detail)
