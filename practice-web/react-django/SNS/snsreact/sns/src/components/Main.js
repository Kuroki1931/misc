import { Inbox } from '@material-ui/icons';
import React, { useContext } from 'react'
import { ApiContext}  from "../context/ApiContext";
import Ask from './Ask';
import InboxDM from './InboxDM';
import Profile from './Profile';
import ProfileManager from './ProfileManager';


const Main = () => {
    const { profiles, profile, askList, askListFull, inbox } = useContext(ApiContext);
    const filterProfiles = profiles.filter((prof) => {
        return prof.id !== profile.id;
    })
    const listProfiles =
        filterProfiles &&
        filterProfiles.map((filprof) => (
            <Profile
                key={filprof.id}
                profileData={filprof}
                askData={askListFull.filter((ask) => {
                    return (
                      (filprof.userPro === ask.askFrom) | (filprof.userPro === ask.askTo)
                    );
                  })}
            />
        ));

    

    return (
        <div>
            <container>
              <h1>Member List</h1>
              <div>{listProfiles}</div>
            </container>

            <container>
                <div>
                    <ProfileManager />
                </div>
            </container>

            <container>
                <h1>承認</h1>
                {profile.id &&
                  askList.map((ask) => (
                      <Ask 
                        key={ask.id}
                        ask={ask}
                        prof={profiles.filter((item)=> {
                            return item.userPro === ask.askFrom
                        })}
                      />
                  ))}
            </container>

            <contaiener>
                <h1>Messagebox</h1>
                {profile.id &&
                  inbox.map((dm) => (
                      <InboxDM 
                        key={dm.id}
                        dm={dm}
                        prof={profiles.filter((item) => {
                            return item.userPro === dm.sender;
                        })}
                        />
                  ))}
            </contaiener>
        </div>  
    )
}

export default Main
