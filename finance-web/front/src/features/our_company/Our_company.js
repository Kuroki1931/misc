import React from 'react'
import classes from './Our_company.module.css'
import head_icon from './team.jpeg'

const Our_company = () => {
    return (
        <div>
            <div className={classes.head_box}>
                <img src={head_icon} className={classes.head_icon}/>
                <div className={classes.head_font}>東大金融会とは</div>
            </div>
            <div className={classes.body_all}>
                <div className={classes.topic_head}>
                    紹介スライド
                </div>
                <div className={classes.slide}>
                    <iframe className={classes.pc_slide} src="https://docs.google.com/presentation/d/e/2PACX-1vSjLvMXk4bkaLzll12UGCgKONspPgqHpEwFR2-n6xQw15Uv4unQI8ld86fdCU5ATx5IcXVk2beRTeJW/embed?start=false&loop=false&delayms=3000" frameborder="0" width="900" height="600" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
                    <iframe className={classes.phone_slide} src="https://docs.google.com/presentation/d/e/2PACX-1vSjLvMXk4bkaLzll12UGCgKONspPgqHpEwFR2-n6xQw15Uv4unQI8ld86fdCU5ATx5IcXVk2beRTeJW/embed?start=false&loop=false&delayms=3000" frameborder="0" width="300" height="200" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
                </div>
            </div>
        </div>
    )
}

export default Our_company
