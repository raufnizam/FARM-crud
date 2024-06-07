// TodoList.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import TodoListView from './TodoListView';

function TodoList() {
    const [todoList, setTodoList] = useState([]);
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    useEffect(() => {
        axios.get('http://localhost:8000/api/todo')
            .then(res => {
                setTodoList(res.data);
            })
            .catch(error => {
                console.error('Error fetching todos:', error);
            });
    }, []);

    const addTodoHandler = () => {
        axios.post('http://localhost:8000/api/todo', {
            title: title,
            description: description
        })
            .then(res => {
                console.log(res);
                setTodoList([...todoList, res.data]);
            })
            .catch(error => {
                console.error('Error adding todo:', error);
            });
    };

    return (
        <div>
            <h1>Todo List</h1>
            <div className="form">
                <input
                    type="text"
                    placeholder="Title...."
                    value={title}
                    onChange={event => setTitle(event.target.value)}
                />
                <input
                    type="text"
                    placeholder="Description...."
                    value={description}
                    onChange={event => setDescription(event.target.value)}
                />
                <button onClick={addTodoHandler}>Add Task</button>
            </div>
            <h1>Your Tasks</h1>
            <TodoListView todoList={todoList} />
        </div>
    );
}

export default TodoList;
