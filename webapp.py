import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)

st.title("My Todo App")

todos = functions.get_todos()
for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        # rerun required
        st.experimental_rerun()



st.text_input(label="",placeholder="add a todo here",
              on_change=add_todo,key="new_todo")
st.session_state
print("hello2")