FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """
    reads the text file and returns the data
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """
    writes into the textfile and the content is give by todos-arg
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ =="__main__":
    print("This is not module")

# while importng it its __name__ becomes functions in the file we are working on
# if __name__ == "functions":
#     print("This is a module")