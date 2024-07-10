
def start_menu():
    print("\nWelcome to the To-Do List Application\n")
    print("Menu: ")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Quit")

start_menu()

def add_tasks(tasks):
    task_id = input("Enter the task to complete: ")
    tasks.append(f"Task: {task_id}, status: Incomplete")
    print(f"Task: {task_id} was added with an Incomplete status ")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list")
    else:
        counter = 1
        for task in tasks:
            counter += 1
            print(f"{counter}. {task}, status: Incomplete")


def run_app():
    start_menu() 
    tasks = []
    while True: 
        selection = input("Enter your menu selection: ")
        if selection == "1":
            add_tasks(tasks)
        elif selection == "2":
            view_tasks(tasks)
        elif selection == "3":
            status_tasks(tasks)
        elif selection == "4":
            delete_tasks(tasks)
        elif selection == "5":
            print("The application is shutting down. Goodbye!") 
            print(f"This is your task list: {tasks}")
            break
        else: 
            print("Invalid option. Please make another selection.")


run_app()           





