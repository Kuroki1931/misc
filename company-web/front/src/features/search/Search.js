import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from "react-redux";
import { Link } from 'react-router-dom';
import classes from './Search.module.css';
import App_bar from '../app_bar/App_bar';

import {
    fetchAsynCampanyList_Get,
    selectCompany_list
} from "../company/companySlice";
import Footer from '../footer/Footer';


const Search = () => {
    const dispatch = useDispatch();

    const other_id = (number) => {
        let dir = window.location.href.split("/");
        let dir2 = dir[dir.length - number];
        return dir2;
    }
    const taget_cate = other_id(2) == 'search' ? '' : decodeURI(other_id(2))
    const company_list = useSelector(selectCompany_list).filter((output) => {
        return output.category.match(taget_cate);
    })
  

    useEffect(async() => {
        dispatch(fetchAsynCampanyList_Get())
    }, []);
    
    return (
        <div>
            <header>
                <App_bar/>
            </header>
            <div className={classes.company_head}>
                東大生が注目する企業{company_list.length}社
            </div>
            <div style={{marginLeft: '20px'}}>参照: {company_list.length}社 {company_list.length*3 + company_list.length*5}記事</div>
            <div className={classes.content}>
                <div className={classes.right_box}>
                    <div className={classes.right_box_box}>
                        <div className={classes.search_head}>
                            業界検索
                        </div>
                        <ul>
                            <Link to={`/search/商社/`}　style={{ textDecoration: 'none', color: '#424242' }}>
                                <li>商社</li>
                            </Link>
                            <Link to={`/search/コンサル/`}　style={{ textDecoration: 'none', color: '#424242' }}>
                                <li>コンサル</li>
                            </Link>
                            <Link to={`/search/シンクタンク/`}　style={{ textDecoration: 'none', color: '#424242' }}>
                                <li>シンクタンク</li>
                            </Link>
                            <Link to={`/search/不動産/`}　style={{ textDecoration: 'none', color: '#424242' }}>
                                <li>不動産</li>
                            </Link>
                            <Link to={`/search/メーカー/`}　style={{ textDecoration: 'none', color: '#424242' }}>
                                <li>メーカー</li>
                            </Link>
                            <Link to={`/search/`}　style={{ textDecoration: 'none', color: '#424242' }}>
                                <li>all</li>
                            </Link>  
                        </ul>  
                        <div className={classes.search_head}>
                            属性比較
                        </div>
                        <ul>
                            <Link to={`/property/給与/`}　style={{ textDecoration: 'none', color: '#424242' }}>
                                <li>給与</li>
                            </Link>
                            <Link to={`/property/休暇/`}　style={{ textDecoration: 'none', color: '#424242' }}>
                                <li>休暇</li>
                            </Link>
                            <Link to={`/property/勤務地/`}　style={{ textDecoration: 'none', color: '#424242' }}>
                                <li>勤務地</li>
                            </Link>
                        </ul>             
                    </div>
                </div>
                <div className={classes.left_box}>
                <div className={classes.company_head}>
                    {taget_cate == '' ? '企業一覧' : `${taget_cate}一覧` }
                </div>
                    {company_list.length != 0 &&
                        company_list.map((each_info) => (
                            <Link to={`/company/${each_info.id}/`}　className={classes.company_box} style={{ textDecoration: 'none', color: '#424242' }}>
                                <div className={classes.company_font}>{each_info.name}</div>
                                <div className={classes.keyword_position}>
                                    <span className={classes.keyword}>{each_info.keywords['keyword0']}</span>
                                    <span className={classes.keyword}>{each_info.keywords['keyword1']}</span>
                                    <span className={classes.keyword}>{each_info.keywords['keyword2']}</span>
                                    <span className={classes.keyword}>{each_info.keywords['keyword3']}</span>
                                    <span className={classes.keyword}>{each_info.keywords['keyword4']}</span>
                                    <span className={classes.keyword}>{each_info.keywords['keyword5']}</span>
                                    <span className={classes.keyword}>{each_info.keywords['keyword6']}</span>
                                </div>
                            </Link>
                        ))
                    }
                </div>
            </div>
            <Footer />
        </div>
    )
}

export default Search
