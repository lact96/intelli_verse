// src/components/CourseForm.js
import React, { useState, useContext } from 'react';
import api from '../api';
import AuthContext from '../context/AuthContext';

function CourseForm({ course, setCourses }) {
    const { authTokens } = useContext(AuthContext);
    const [title, setTitle] = useState(course ? course.title : '');
    const [description, setDescription] = useState(course ? course.description : '');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newCourse = { title, description };
        if (course) {
            // Update existing course
            api.put(`/courses/${course.id}/`, newCourse, {
                headers: {
                    'Authorization': `Bearer ${authTokens.access}`
                }
            }).then(response => {
                setCourses(prevCourses => prevCourses.map(c => (c.id === course.id ? response.data : c)));
            }).catch(error => console.error('Error updating course:', error));
        } else {
            // Create new course
            api.post('/courses/', newCourse, {
                headers: {
                    'Authorization': `Bearer ${authTokens.access}`
                }
            }).then(response => {
                setCourses(prevCourses => [...prevCourses, response.data]);
            }).catch(error => console.error('Error creating course:', error));
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
                placeholder="Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />
            <button type="submit">{course ? 'Update' : 'Create'}</button>
        </form>
    );
}

export default CourseForm;
