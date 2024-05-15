// src/components/LessonList.js
import React, { useEffect, useState, useContext } from 'react';
import api from '../api';
import LessonForm from './LessonForm';
import AuthContext from '../context/AuthContext';

function LessonList() {
    const { authTokens } = useContext(AuthContext);
    const [lessons, setLessons] = useState([]);
    const [selectedLesson, setSelectedLesson] = useState(null);

    useEffect(() => {
        api.get('/lessons/')
            .then(response => {
                setLessons(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the lessons!', error);
            });
    }, []);

    const deleteLesson = (id) => {
        api.delete(`/lessons/${id}/`, {
            headers: {
                'Authorization': `Bearer ${authTokens.access}`
            }
        }).then(() => {
            setLessons(lessons.filter(lesson => lesson.id !== id));
        }).catch(error => console.error('Error deleting lesson:', error));
    };

    return (
        <div>
            <h1>Lessons</h1>
            <LessonForm setLessons={setLessons} lesson={selectedLesson} />
            <ul>
                {lessons.map(lesson => (
                    <li key={lesson.id}>
                        {lesson.title}
                        <button onClick={() => setSelectedLesson(lesson)}>Edit</button>
                        <button onClick={() => deleteLesson(lesson.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default LessonList;
