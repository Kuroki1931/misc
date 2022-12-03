import React, { useContext } from 'react'
import { ApiContext } from "../context/ApiContext";


const Profile = ({profileData, askData}) => {
    const { newRequestFriend, profile } = useContext(ApiContext)

    const newRequest = () => {
        const askUploadData = new FormData();
        askUploadData.append('askTo', profileData.userPro)
        newRequestFriend(askUploadData)
    }
    

    return (
        <div>
            {profileData.img ? (
                <img src={profileData.img} width="15%" />
            ) : (
                <img
                    src="https://www.google.com/search?q=no+image&rlz=1C1QABZ_jaJP901JP901&tbm=isch&source=iu&ictx=1&fir=FZXKCHY0sdAZeM%252CUGLRiMygoEPsCM%252C_&vet=1&usg=AI4_-kRoQgqBF2GJmTtdsrRPaLXsvbv85w&sa=X&ved=2ahUKEwiHt6zkkv_tAhXVMN4KHdOZChAQ9QF6BAgPEAE#imgrc=FZXKCHY0sdAZeM"
                />
            )}
            <div>{profileData.nickName}</div>
            <div>{profileData.created_on}</div>

            <container>
                {!askData[0] && profile.id ? (
                    <button
                      onClick={() => newRequest()}
                    >
                        Ask as friend
                    </button>
                ) : (
                    <button
                      disabled
                    >
                        Ask as friend
                    </button>
                )}
            </container>
        </div>
    )
}

export default Profile
