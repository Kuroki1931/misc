import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from "react-redux";
import classes from './Company.module.css';
import news_icon from './news_pic.jpeg';

import {
    fetchAsynCampany_Get,
    selectCompany_info,
} from "../company/companySlice";

const Company = () => {
    const dispatch = useDispatch();
    const company = useSelector(selectCompany_info);
    
    const other_id = (number) => {
        let dir = window.location.href.split("/");
        let dir2 = dir[dir.length - number];
        return dir2;
    }

    useEffect(async() => {
        dispatch(fetchAsynCampany_Get(other_id(2)))
    }, [dispatch]);

    
    return (
        <div>
            <header className={classes.header}>
                <div>{company.name}</div>
            </header>
            {company.keywords != null &&
                <div>
                    <h2 className={classes.head}>Keywords</h2>
                    <div className={classes.keyword_explain}>複数の記事を自然言語処理にかけkeywordを抽出。</div>
                    <div className={classes.keyword_box}>
                    <br/>
                        {Object.keys(company.keywords).map((each) => (
                            <div className={classes.keyword_position}>
                                <div className={classes.keyword}>{company.keywords[each]}</div>
                            </div>
                        ))}
                    </div>
                </div>
            }
            {company.recruit != null &&
                <div>
                    <h2 className={classes.head}>募集要項</h2>
                    <div className={classes.table_box}>
                        {Object.keys(company.recruit).map((each) => (
                            <dl>
                                <dt className={classes.tag_dt}>{each}</dt>
                                <dt>{company.recruit[each]}</dt>
                            </dl>
                        ))}
                    </div>
                </div>
            }
            {company.news != 0 &&
                <div>
                    <h2 className={classes.head}>注目記事まとめ</h2>
                    <div className={classes.news_box}>
                        {Object.keys(company.news).map((each) => (
                            <div className={classes.news_all}>
                                <div className={classes.each_news}>
                                    <img src={news_icon} className={classes.news_icon}/>
                                    <div className={classes.news_card}>
                                    </div>
                                    <div  className={classes.news_position}>
                                        <a href={company.news[each]} className={classes.news}>{each}</a>
                                    </div>
                                </div>
                            </div>
                        ))}    
                    </div>
                </div>
            }
            <footer className={classes.header}>
                <div>{company.name}</div>
            </footer>
        </div>
    )
}

export default Company
