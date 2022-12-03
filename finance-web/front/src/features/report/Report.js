import React, { useEffect } from 'react';
import { useSelector, useDispatch } from "react-redux";
import { withCookies } from "react-cookie";
import { Link } from 'react-router-dom';
import classes from "./Report.module.css";
import Search_bar from './Search_bar';
import Search_bar_name from './Search_bar_name';
import Button from '@material-ui/core/Button';
import head_icon from './street.jpeg'
import Card from '@material-ui/core/Card';
import {HashLink} from 'react-router-hash-link'


import {
    selectCompany_list,
    fetchAsyncCompnay_listGet,
    selectPDF_list,
    fetchAsyncPDF_listGet,
    selectCompany,
    fetchAsyncCompnayGet,
    selectError,
} from "./reportSlice";


const Report = (props) => {
    const dispatch = useDispatch();
    const token = props.cookies.get("current-token");
    const company_list = useSelector(selectCompany_list)
    const company = useSelector(selectCompany)
    const error = useSelector(selectError)
    const pdf_list = useSelector(selectPDF_list);
    const take_url = (number) => {
        let dir = window.location.href.split("/");
        let dir2 = dir[dir.length - number];
        return dir2;
    }
    const uuid = take_url(2)

    useEffect(() => {
        dispatch(fetchAsyncPDF_listGet(token))
        dispatch(fetchAsyncCompnay_listGet())
        dispatch(fetchAsyncCompnayGet(uuid))
    }, [dispatch, uuid]);

    const target_company = pdf_list.filter((output) => {
        return output.company == uuid
    })
    const basic_report = target_company.filter((output) => {
        return output.pdf_type == 0
    })
    const deep_report = target_company.filter((output) => {
        return output.pdf_type == 1
    })
    const short_report = target_company.filter((output) => {
        return output.pdf_type == 2
    })
    

    return (
        <div>
            <div className={classes.head_box}>
                <img src={head_icon} className={classes.head_icon}/>
                <div className={classes.head_font}>企業レポート</div>
            </div>
            <div id="piyo" className={classes.body_all}>
                <div className={classes.info_box}>
                    <div className={classes.search_box}>
                        <div className={classes.search_bar}>
                            <Search_bar company_list={company_list}/>
                        </div>
                        <div className={classes.search_bar}>
                            <Search_bar_name company_list={company_list}/>
                        </div>
                    </div>
                </div>
                <div>
                    <div className={classes.target_company_box}>
                    <div className={classes.target_company_name}>{company.company_name} {company.company_number} </div>
                        {basic_report != 0 &&
                            <div>
                                <div className={classes.report_head}>
                                    シンプルベーシックレポート
                                </div>
                                <div className={classes.report_box}>
                                    <a href={'https' + basic_report[0].pdf.slice(4)}>{basic_report[0].regist_date.slice(0, 10)}</a>
                                    <Button variant="contained" color="primary" style={{marginLeft: '30px'}}>
                                        <a href='https://docs.google.com/forms/d/e/1FAIpQLSdeCHL6DYzxUk333QPV7yn0vn1yAh0vkGOvJECTmR7i232XKQ/viewform?usp=sf_link'　style={{color: '#fff'}}>質問する</a>
                                    </Button>
                                </div>
                            </div>
                        }
                        {deep_report != 0 &&
                            <div>
                                <div className={classes.report_head}>
                                    ディープレポート
                                </div>
                                <div className={classes.report_box}>
                                    <a href={'https' + deep_report[0].pdf.slice(4)}>{deep_report[0].regist_date.slice(0, 10)}</a>
                                    <Button variant="contained" color="primary" style={{marginLeft: '30px'}}>
                                        <a href='https://docs.google.com/forms/d/e/1FAIpQLSdeCHL6DYzxUk333QPV7yn0vn1yAh0vkGOvJECTmR7i232XKQ/viewform?usp=sf_link'　style={{color: '#fff'}}>質問する</a>
                                    </Button>
                                </div>
                            </div>
                        }
                        {short_report != 0 &&
                            <div>
                                <div className={classes.report_head}>
                                    アドホックレポート
                                </div>
                                {short_report.map((each_pdf) => (
                                    <div key={each_pdf.id} className={classes.report_box}>
                                        <a href={'https' + each_pdf.pdf.slice(4)}>{each_pdf.regist_date.slice(0, 10)}</a>
                                        <Button variant="contained" color="primary" style={{marginLeft: '30px'}}>
                                            <a href='https://docs.google.com/forms/d/e/1FAIpQLSdeCHL6DYzxUk333QPV7yn0vn1yAh0vkGOvJECTmR7i232XKQ/viewform?usp=sf_link'　style={{color: '#fff'}}>質問する</a>
                                        </Button>
                                    </div>
                                ))}
                            </div>
                        }
                        <div className={classes.error}>
                            {error}
                        </div>
                    </div>
                    <div className={classes.company_list_box}>
                        {company_list.map((company) => (       
                            <HashLink key={company.id} to={`/report/${company.id}/#piyo`} style={{textDecoration: 'none'}}>                                  
                                <Card className={classes.company_link}>
                                    <div className={classes.company_num}>{company.company_number}</div>
                                    <div>{company.company_name}</div>
                                </Card>                                 
                            </HashLink>
                        ))}
                    </div>
                </div>
                <div className={classes.update_box}>
                        <div className={classes.update_head}>
                            レポートアップデート情報
                        </div>
                        <div className={classes.update_info_box}>
                            <div className={classes.error}>
                                {error}
                            </div>
                            {pdf_list.slice(-4).reverse().map((pdf) => (
                                <div className={classes.update_each_box}>
                                    <div>{pdf.regist_date.slice(0, 10)}</div>
                                    <a href={'https' + pdf.pdf.slice(4)}>{pdf.pdf_title}</a>
                                </div>
                            ))}
                        </div>
                    </div>
            </div>
        </div>
    )
}

export default withCookies(Report)
