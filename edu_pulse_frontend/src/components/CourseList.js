// src/components/CourseList.js
import React, { useEffect, useState, useContext } from 'react';
import api from '../api';
import CourseForm from './CourseForm';
import AuthContext from '../context/AuthContext';

function CourseList() {
    const { authTokens } = useContext(AuthContext);
    const [courses, setCourses] = useState([]);
    const [selectedCourse, setSelectedCourse] = useState(null);

    useEffect(() => {
        api.get('/courses/')
            .then(response => {
                setCourses(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the courses!', error);
            });
    }, []);

    const deleteCourse = (id) => {
        api.delete(`/courses/${id}/`, {
            headers: {
                'Authorization': `Bearer ${authTokens.access}`
            }
        }).then(() => {
            setCourses(courses.filter(course => course.id !== id));
        }).catch(error => console.error('Error deleting course:', error));
    };

    return (
        <div>
            <h1>Courses</h1>
            <CourseForm setCourses={setCourses} course={selectedCourse} />
            <ul>
                {courses.map(course => (
                    <li key={course.id}>
                        {course.title}
                        <button onClick={() => setSelectedCourse(course)}>Edit</button>
                        <button onClick={() => deleteCourse(course.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default CourseList;
