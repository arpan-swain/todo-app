import functions
import time
print(f"Today is {time.strftime('%b %d, %Y  %H:%M:%S')}")
while True:
    user_action = input("Type add, show, edit , complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + "\n")

        functions.write_todos(todos)

        # file = open("todos.txt", "w")
        # file.writelines(todos)
        # file.close()

    elif user_action.startswith("show"):
        # open_todos()
        # show_todos()
        todos = functions.get_todos()
        if len(todos) == 0:
            print("There are no todos!!")
        else:
            print("These are your items")
            for index, item in enumerate(todos):
                # solving the extra newline problem
                item = item.strip("\n")
                item = item.title()
                print(f"{index + 1} : {item}")
            print()
    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()
            if len(todos) == 0:
                print("First add some items")
            else:
                number = int(user_action[5:])
                todos[number - 1] = input("enter the new task : ") + "\n"
                functions.write_todos(todos)
        except ValueError:
            print("That was an Invalid Command!")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()
            if len(todos) == 0:
                print("First add some items")
            else:
                number = int(user_action[9:])
                removed_todo=todos.pop(number-1).strip("\n")
                functions.write_todos(todos)
                print(f"the todo '{removed_todo}' was removed successfully !!")
        except IndexError:
            print("No value with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("You entered unknown command!!")
print("Bye!")
