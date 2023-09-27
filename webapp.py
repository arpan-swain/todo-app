import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)

st.title("My Todo App")

todos = functions.get_todos()
for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="add a todo here",
              on_change=add_todo,key="new_todo")
st.session_state
print("hello2")