import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass
sg.theme("Black")

timeshow = sg.Text("", key = "clock", font=("Helvetica,8"))
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values= functions.get_todos(),key= "todos-list",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do app",
                   layout=[[timeshow],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button,complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, value = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos-list"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = value["todos-list"][0]
                new_todo = value["todo"] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window["todos-list"].update(values=todos)
            except IndexError :
                sg.popup("Select an item then click edit")
        case "complete":
            try:
                todos=functions.get_todos()
                todos.remove(value["todos-list"][0])
                functions.write_todos(todos)
                window["todos-list"].update(values=functions.get_todos())
                window["todo"].update(value="")
            except IndexError :
                sg.popup("Select an item then click edit",font=("Helvetica, 10"))
        case "Exit":
            break
        case "todos-list":
            window["todo"].update(value=value["todos-list"][0])

        case sg.WIN_CLOSED:
            break
window.close()