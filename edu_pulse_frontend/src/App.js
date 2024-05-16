// src/App.js
import React, { useContext } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import VideoFeed from './components/VideoFeed';
import LearningPath from './components/LearningPath';
import UserProfile from './components/UserProfile';
import AuthContext from './context/AuthContext';

function App() {
    const { user, loginUser, logoutUser } = useContext(AuthContext);

    return (
        <Router>
            <div className="App">
                <header className="App-header">
                    <h1>Welcome to EduPulse</h1>
                    {user ? (
                        <>
                            <button onClick={logoutUser}>Logout</button>
                            <p>Logged in as {user.username} {user.username}</p>
                        </>
                    ) : (
                        <form onSubmit={loginUser}>
                            <input type="text" name="username" placeholder="Username" />
                            <input type="password" name="password" placeholder="Password" />
                            <button type="submit">Login</button>
                        </form>
                    )}
                </header>
               {user && <UserProfile />}
               <Routes>
                    <Route path="/videos" element={<VideoFeed />} />
                    <Route path="/learning-path" element={<LearningPath />} />
                    <Route path="/profile" element={<UserProfile />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
