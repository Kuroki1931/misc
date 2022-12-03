import React from 'react'

const InboxDM = ({dm, prof}) => {
    return (
        <div>
            <li>
                {prof[0] && <h4>{dm.message}</h4>}
                {prof[0] && (
                    <h4>
                        {prof[0].nickName}
                    </h4>
                )}
            </li>
        </div>
    )
}

export default InboxDM
