// TodoListView.js
import React from 'react';
import Todo from './Todo';

function TodoListView(props) {
    return (
        <div>
            <ul>
                {props.todoList.map(todo => <Todo key={todo.title} todo={todo} />)}
            </ul>
        </div>
    );
}

export default TodoListView;
