import React, { useContext } from 'react'
import { ApiContext } from "../context/ApiContext";

const ProfileManager = () => {
    const {
        profile,
        editedProfile,
        setEditedProfile,
        deleteProfile,
        cover,
        setCover,
        createProfile,
        editProfile,
    } = useContext(ApiContext)

    const handleInputChange = () => (event) => {
        const value = event.target.value;
        const name = event.target.name;
        setEditedProfile({ ...editedProfile, [name]: value });
      };

  

    return (
        <div>
            <h1>My Profile</h1>
            <div>
                {profile.id ? (
                    <img src={profile.img} width="15%" />
                ) : (
                    <img
                        src="https://www.google.com/search?q=no+image&rlz=1C1QABZ_jaJP901JP901&tbm=isch&source=iu&ictx=1&fir=FZXKCHY0sdAZeM%252CUGLRiMygoEPsCM%252C_&vet=1&usg=AI4_-kRoQgqBF2GJmTtdsrRPaLXsvbv85w&sa=X&ved=2ahUKEwiHt6zkkv_tAhXVMN4KHdOZChAQ9QF6BAgPEAE#imgrc=FZXKCHY0sdAZeM"
                    />
                )}
                <input
                    type="file"
                    id="imageInput"
                    onChange={(event) => {
                        setCover(event.target.files[0]);
                        event.target.value = "";
                    }}
                />
            </div>
            
            {editedProfile.id ? (
                editedProfile.nickName ? (
                <button onClick={() => editProfile()}>
                    editprofile
                </button>
                ) : (
                <button disabled>
                    editprofile
                </button>
                )
            ) : editedProfile.nickName && cover.name ? (
                <button onClick={() => createProfile()}>
                create
                </button>
            ) : (
                <button disabled>
                create
                </button>
            )}
            <button onClick={() => deleteProfile()}>
                trash
            </button>
            <div>
                {profile && <span>{profile.nickName}</span>}
                <hr />
                <input
                type="text"
                value={editedProfile.nickName}
                name="nickName"
                onChange={handleInputChange()}
                />
                <hr />
                <span>Joined at {profile.created_on} </span>
                <hr />
                <span>JAPAN</span>
            </div>
        </div>
    )
}

export default ProfileManager
