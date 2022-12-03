import React from 'react'
import classes from "./Company.module.css";
import { Link } from "react-router-dom";

const Company = () => {
    return (
        <div>
            <div>
                <img
                  src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRaHH3iTi6GOkfPhPbAlh1QrznVBu9Xmf8brg&usqp=CAU'
                  alt='会社画像'
                />
            </div>
            <div
              style={{ padding: '60px 0 60px 0', borderBottom: '1px solid #0095aa'}}
              id="topMission"
            >
                <h3　className={classes.Title}>
                    Mission
                </h3>
                <h3 className={classes.subtitle}>
                    教育に、人に、社会に
                    <br/>
                    次の可能性を。
                </h3>
                <div className={classes.container}>
                    <p>
                        教育を新しくすること。それは、社会の真ん中を新しくすること。
                        <br/>
                        私たちは学びのあり方を進化させます。
                    </p>
                    <p>
                    　　学習を一人ひとり最適化し、「基礎学力」を最短で身につける。
                        <br/>
                        そのぶん増える時間で、「社会でいきる力」を伸ばす。
                    </p>
                    <p>
                    　　それが私たちの目指すもの。
                        <br/>
                        自分の人生を生きる人を増やし、これからの社会をつくっていきます。
                    </p>
                </div>
                <div>
                    <img 
                        style={{padding: "60px 0 0 0"}}
                        src='https://static.retrip.jp/article/122754/images/12275498d69d0f-52b6-4043-b958-a76066f5b263_l.jpg'
                        alt='no images'
                    />
                    <h3　className={classes.Title}>
                        Vision
                    </h3>
                    <h3 className={classes.subtitle}>
                        Wow students.
                    </h3>
                    <h3>
                        生徒が熱狂する学びを。
                    </h3>
                    <h3>
                        勉強をワクワクするもの、自分からやりたいものに変え、
                        <br/>
                        生徒一人ひとりの可能性を広げる。
                        <br/>
                        私たちのあらゆる行動は、ただ、そのためにあります。
                    </h3>
                </div>
            </div>
            <div id="topMembers">
                <h3　className={classes.Title}>
                    Members
                </h3>
                <h3 style={{ color: "#0095aa", fontsize: "60px", display: "block"}}>
                    一人ひとりをご紹介します。
                </h3>
                <nav>
                    <a href='https://www.atama.plus/members/'>
                        <img 
                            style={{width: '80%'}}
                            src='https://www.atama.plus/wp-content/themes/atamaplus/image/bnr_members.jpg' 
                            alt='no-images'
                        />
                    </a>
                    <a className={classes.pro} href='https://www.atama.plus/members/' style={{display: 'block'}}>
                        Profile
                    </a>
                </nav>
            </div>
            <div style={{ padding:'60px'}} id="corporate">
                <h3　className={classes.Title}>
                    Corporate info
                </h3>
                <dl>
                    <dt>
                        <span>社</span>
                        <span>名</span>
                    </dt>
                    <dd>atama plus 株式会社</dd>
                    <dt>
                        <span>設</span>
                        <span>立</span>
                    </dt>
                    <dd> 2017年4月3日</dd>
                    <dt>
                        <span>所</span>
                        <span>在</span>
                        <span>地</span>
                    </dt>
                    <dd> 東京都品川区西五反田4-31-18 目黒テクノビル2F</dd>
                </dl>
                <iframe
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3243.0458497246987!2d139.71152185061078!3d35.62659618010995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60188951fc1551ef%3A0x995ddffb0504f332!2zYXRhbWEgcGx1cyDmoKrlvI_kvJrnpL4!5e0!3m2!1sja!2sjp!4v1607863166303!5m2!1sja!2sjp"
                    width="100%"
                    height="450"
                    frameBorder="0"
                    style={{ border: "0" }}
                    allowFullScreen=""
                    aria-hidden="false"
                    tabIndex="0"
                    title="Map"
                ></iframe>
            </div>
            

            
            
            
        </div>
    )
}

export default Company
