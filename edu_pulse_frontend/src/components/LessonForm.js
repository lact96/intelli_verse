// src/components/LessonForm.js
import React, { useState, useContext } from 'react';
import api from '../api';
import AuthContext from '../context/AuthContext';

function LessonForm({ lesson, setLessons }) {
    const { authTokens } = useContext(AuthContext);
    const [title, setTitle] = useState(lesson ? lesson.title : '');
    const [content, setContent] = useState(lesson ? lesson.content : '');
    const [videoUrl, setVideoUrl] = useState(lesson ? lesson.video_url : '');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newLesson = { title, content, video_url: videoUrl };
        if (lesson) {
            // Update existing lesson
            api.put(`/lessons/${lesson.id}/`, newLesson, {
                headers: {
                    'Authorization': `Bearer ${authTokens.access}`
                }
            }).then(response => {
                setLessons(prevLessons => prevLessons.map(l => (l.id === lesson.id ? response.data : l)));
            }).catch(error => console.error('Error updating lesson:', error));
        } else {
            // Create new lesson
            api.post('/lessons/', newLesson, {
                headers: {
                    'Authorization': `Bearer ${authTokens.access}`
                }
            }).then(response => {
                setLessons(prevLessons => [...prevLessons, response.data]);
            }).catch(error => console.error('Error creating lesson:', error));
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
            />
            <textarea
                placeholder="Content"
                value={content}
                onChange={(e) => setContent(e.target.value)}
            />
            <input
                type="text"
                placeholder="Video URL"
                value={videoUrl}
                onChange={(e) => setVideoUrl(e.target.value)}
            />
            <button type="submit">{lesson ? 'Update' : 'Create'}</button>
        </form>
    );
}

export default LessonForm;
