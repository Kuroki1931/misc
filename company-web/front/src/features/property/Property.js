import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from "react-redux";
import classes from './Property.module.css';

import {
    fetchAsynCampanyList_Get,
    selectCompany_list,
} from "../company/companySlice";

const Property = () => {
    const dispatch = useDispatch();
    const company_list = useSelector(selectCompany_list)

    // urlの取り出し
    const other_id = (number) => {
        let dir = window.location.href.split("/");
        let dir2 = dir[dir.length - number];
        return dir2;
    }

    const target_dic = {'給与': ['初任給'], '休暇': ['休日', '休暇'], '勤務地': ['勤務地'] }
    const target = target_dic[decodeURI(other_id(2))]

    useEffect(async() => {
        dispatch(fetchAsynCampanyList_Get())
    }, []);

    return (
        <div>
            <header className={classes.header}>
                <div>{decodeURI(other_id(2))}</div>
            </header>
            <div>
                <h2 className={classes.head}>{decodeURI(other_id(2))}一覧</h2>
                <div className={classes.property_box}>
                    {company_list.map((company) => (
                        Object.keys(company.recruit).map((tab) => {
                            for (let i = 0; i < target.length; i++){
                                if (tab.match(target[i])){
                                    return (
                                    <dl className={classes.tag_dl}>
                                        <dt className={classes.tag_dt}>{company.name}</dt>
                                        <dd className={classes.tag_dd}>{company.recruit[tab]}</dd>
                                    </dl>
                                    )
                                break;
                                }
                            }
                        })
                    ))}
                </div>
            </div>
           
            <footer className={classes.header}>
                <div>{decodeURI(other_id(2))}</div>
            </footer>
        </div>
    )
}

export default Property