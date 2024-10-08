todo_list = []

def add_task(t):
    todo_list.append(str(t))


def show_task():
    for i in todo_list:
        print(i)

