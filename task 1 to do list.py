# initialize an empty list to store tasks
tasks=[]
#function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"task '{task}'has been added to the to-do list.")
#function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"task '{task}'has been removed from the to-do list.")
    else:
        print(f"task '{task}'not found in the to-do list.")
#function to display the to-do list
def display_tasks():
    if tasks:
        print("to-do list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}.{task}")
    else:
        print("your to-do list is empty.")
#main program loop
while True:
    print("\nmenu:")
    print("1. add a task")
    print("2. remove a task")
    print("3. display tasks")
    print("4. quit")
    choice = input("enter your choice:")
    if choice =='1':
        task = input("enter the task:")
        add_task(task)
    elif choice =='2':
        task=input("enter the task to remove:")
        remove_task(task)
    elif choice =='3':
        display_tasks()
    elif choice =='4':
        break
    else:
        print("invalid choice. please select a valid optiion.")
    print("goodbye!")
    


