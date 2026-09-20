todo = ['This is a task', 'Do this']

def show():
    [print (*(f"{ind+1}: {i}"for ind, i in enumerate(todo)), sep="\n")]

def delTask():
    show()
    delT = input("Which task? ")
    todo.pop(int(delT)-1)
    return(show())

def add():
    task = input("What is the task? ")
    todo.append(task)
    return(show())

while True:
    print("1: Add Task\n2: Delete Task\n3: Show Tasks\n4: Exit")
    choice = input("Choice: ")
    if(choice == "1"):
        add()
    elif(choice == "2"):
        delTask()
    elif(choice == "3"):
        show()
    elif(choice == "4"):
        break
    else:
        print("Choose from 1,2,3,4")
    print("\n")