// frontend/src/Profile.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Profile = () => {
    const [profile, setProfile] = useState({});

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/profiles/')
            .then(response => {
                // Assuming there's only one profile, we take the first one
                if (response.data.length > 0) {
                    setProfile(response.data[0]);
                }
            })
            .catch(error => console.error('There was an error fetching the profile!', error));
    }, []);

    return (
        <div>
            {profile ? (
                <div>
                    <p>{profile.bio}</p>
                </div>
            ) : (
                <p>Loading profile...</p>
            )}
        </div>
    );
};

export default Profile;
