import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    newtodo = st.session_state['new_todo'] + '\n'
    todos.append(newtodo)
    functions.write_todos(todos)

st.title('My ToDo App')
st.subheader('This is my ToDo app.')
st.write('This app helps increase your productivity.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Enter a ToDo', placeholder='Add new ToDo...', on_change=add_todo, key='new_todo')
