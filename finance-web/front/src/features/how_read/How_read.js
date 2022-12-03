import classes from './How_read.module.css'
import React from 'react'
import head_icon from './read.jpeg'

const How_read = () => {
    return (
        <div>
            <div>
                <img src={head_icon} className={classes.head_icon}/>
                <div className={classes.head_font}>読み方</div>
            </div>
            <div className={classes.body_all}>
                <div className={classes.main_box}>
                    <div className={classes.service}>
                        <div className={classes.each_head}>サービス概要</div>
                        <div>本レポートはプロの投資家として市場で長年戦ってきた運用者が一般投資家に一目でわかるレポートを個人投資家に届けたいとの思いから作成されたものです。日本再考基盤では、”世の中の非効率性を改善したい”との想いを信念として、様々な分野での挑戦を続けてきておりますが、本サイトではプロの視点を極力図示し、かつポイントを明確にして、個人投資家の方にもプロと同じ目線で銘柄を見れるように啓蒙することを目指しています。</div>
                    </div>
                    <br/>
                    <div className={classes.report}>
                        <div className={classes.each_head}>レポートの構成</div>
                        <div className={classes.report_box}>
                            <div className={classes.each_report_box}>
                                <div className={classes.each_report_head}>ベーシックレポート</div>
                                <div>四季報では物足りない、運用者の視点でもう少し簡単に銘柄の見方やバリュエーションをどう考えるか知りたいとのニーズに応えて、簡単に5分で読破できる構成になっている。</div>
                            </div>
                            <div className={classes.each_report_box}>
                                <div className={classes.each_report_head}>ディープレポート</div>
                                <div>企業側からの依頼をベースに、より本質的で、より詳細なものを企業の決算説明資料以外で作成することを試みたもの。こちらについては、企業からの依頼ということもあり、こちらのHPでも無料で公開している。</div>
                            </div>
                            <div className={classes.each_report_box}>
                                <div className={classes.each_report_head}>アドホックレポート</div>
                                <div>注目すべき決算、昨今注目されている事業などに焦点を絞り不定期で出す短いレポート。ヘッジファンド・マネージャーが実際の企業とのやりとりで繰り出したQ&Aなども掲載してリアル感、運用者の興味などを個人投資家にも理解できるようにした。</div>
                            </div>
                        </div>
                    </div>
                    <br/>
                    <div className={classes.question}>
                        <div className={classes.each_head}>質問機能</div>
                        <div>業界でも初の試みとして、質問を受け付けるプレミアムコースも設定している。</div>
                        <div style={{marginTop: '40px'}}>ただし以下に該当する質問は引き受けられない</div>
                        <ul className={classes.except}>
                            <li>1.投資判断に関するもの、若しくは付随するもの</li>
                            <li>2.企業がIR活動をしてない（サイレント期間）における企業とのやりとりの必要性があるもの</li>
                            <li>3.企業から未開示の情報や数字</li>
                            <li>4.その他、当社が回答するのに的確ではないと判断したもの</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default How_read
