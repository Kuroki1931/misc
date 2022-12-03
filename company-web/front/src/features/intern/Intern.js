import React from 'react';
import Footer from '../footer/Footer';
import footer_logo from '../app_bar/東大金融研究会_ロゴ.png';
import line_logo from './line.jpg';
import { Link } from 'react-router-dom';
import classes from './Intern.module.css';
const Intern = () => {
    return (
        <div>
            <footer className={classes.header_box}>
                <img src={footer_logo} className={classes.logo}/>
                <Link className={classes.link} to='/'>インターン</Link>
                <Link className={classes.link} to='/search/'>注目企業</Link>
            </footer>
            <div></div>
            <div>
                <div className={classes.intern_head}>
                    会員の過去のインターン参加実績
                </div>
                <ul className={classes.intern_ul}>
                    <li className={classes.intern_li}>BtoCオンラインサービス会社、上場、経営企画＆データ分析など、2名</li>
                    <li className={classes.intern_li}>BtoB AI＊不動産会社、上場、経営企画、2名</li>
                    <li className={classes.intern_li}>定量コンサルティング、上場、データサイエンス＆コンサルティング、8名</li>
                    <li className={classes.intern_li}>物流系コンサルティング、非上場、コンサルティング、10名</li>
                    <li className={classes.intern_li}>シェアリングビジネス会社、非上場、経営企画＆マーケティングなど、10名</li>
                    <li className={classes.intern_li}>国内運用会社、非上場、運用部、8名</li>
                    <li className={classes.intern_li}>グローバル大手HF、非上場、運用部、1名</li>
                    <li className={classes.intern_li}>日系大手証券会社、非上場、トレーディング、2名</li>
                    <li className={classes.intern_li}>アクティビストファンド、非上場、運用部、1名</li>
                    <li className={classes.intern_li}>国内HF、非上場、運用部、1名</li>
                    <li className={classes.intern_li}>コンサルティング会社、上場、アナリスト、5名</li>
                    <li className={classes.intern_li}>SaaS会社、上場、データ分析＆マーケティング、2名</li>
                    <li className={classes.intern_li}>サービス会社、非上場、人事など、1名</li>
                    <li className={classes.intern_li}>オールタナティブデータ会社、非上場、アナリスト、1名</li>
                </ul>
            </div>
            <div>
                <div className={classes.intern_head}>
                    連絡先
                </div>
                <div>
                    <div className={classes.call_info}>入会希望の方は以下からLineで友達登録を行い、登録先に自己紹介と入会の意思を伝えてください！皆様のご連絡をお待ちしております！</div>
                    <div className={classes.call_box}>
                        <a href='https://line.me/ti/p/dkQ0HcUjh7' className={classes.call_tag}>Lineで友達登録</a>
                        <img src={line_logo} className={classes.call_logo}/>
                    </div>
                </div>
            </div>
            <Footer />
        </div>
    )
}

export default Intern
