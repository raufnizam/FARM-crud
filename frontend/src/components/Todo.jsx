import React, { useState } from 'react';
import axios from 'axios';

function Todo(props) {
    const [deleted, setDeleted] = useState(false); // State to track whether the todo is deleted

    const deleteTodoHandler = () => {
        const title = props.todo.title;
        axios.delete(`http://localhost:8000/api/todo/${title}`)
            .then(res => {
                console.log(res.data);
                // Update state to indicate that the todo is deleted
                setDeleted(true);
            })
            .catch(error => {
                console.error('Error deleting todo:', error);
            });
    };

    if (deleted) {
        // If todo is deleted, don't render it
        return null;
    }

    return (
        <div>
            <p>
                <span>{props.todo.title} : </span> {props.todo.description}
                <button onClick={deleteTodoHandler}>Delete</button>
            </p>
        </div>
    );
}

export default Todo;
