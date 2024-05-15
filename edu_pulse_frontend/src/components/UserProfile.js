// src/components/UserProfile.js
import React, { useEffect, useState, useContext } from 'react';
import api from '../api';
import AuthContext from '../context/AuthContext';

function UserProfile() {
    const { user, authTokens } = useContext(AuthContext);
    const [profile, setProfile] = useState(null);

    useEffect(() => {
        if (user) {
            api.get(`/users/${user.user_id}/`, {
                headers: {
                    'Authorization': `Bearer ${authTokens.access}`
                }
            })
            .then(response => {
                setProfile(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the user profile!', error);
            });
        }
    }, [user, authTokens]);

    if (!profile) return <div>Loading...</div>;

    return (
        <div>
            <h2>{profile.username}</h2>
            <p>Email: {profile.email}</p>
            <p>Bio: {profile.userprofile.bio}</p>
            {profile.userprofile.avatar && <img src={profile.userprofile.avatar} alt="avatar" />}
        </div>
    );
}

export default UserProfile;
