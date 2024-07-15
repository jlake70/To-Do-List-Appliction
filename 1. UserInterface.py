
def start_menu():
    print("\nWelcome to the To-Do List Application\n")
    print("Menu: ")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Quit")

#start_menu()

def add_tasks(tasks):
    task_id = input("Enter the task to complete: ")
    tasks.append({'title': task_id, 'status': 'Incomplete'})
    print(f"Task: {task_id} was added with an Incomplete status ")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list")  
    else:
        counter = 0
        for task in tasks:
            counter += 1
            print(f"{counter}. {task}")

def mark_task_complete(tasks):
    if not tasks:
        print("No tasks to mark as complete.")
        return

    view_tasks(tasks)

    def get_valid_task_number():
        while True:
            try:
                task_number = int(input("Enter the task number to mark as complete: "))
                if 0 < task_number <= len(tasks):
                    return task_number
                else:
                    print("Invalid task number. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    task_number = get_valid_task_number()
    tasks[task_number - 1]['status'] = 'Complete'
    print(f"Task {task_number} marked as complete.")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks(tasks)

    def get_valid_task_number():
        while True:
            try:
                task_number = int(input("Enter the task number to delete: "))
                if 0 < task_number <= len(tasks):
                    return task_number
                else:
                    print("Invalid task number. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    task_number = get_valid_task_number()
    deleted_task = tasks.pop(task_number - 1)
    print(f"Task '{deleted_task['title']}' deleted.")


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
            mark_task_complete(tasks)
        elif selection == "4":
            delete_task(tasks)
        elif selection == "5":
            print("The application is shutting down. Goodbye!") 
            print(f"This is your task list: {tasks}")
            break
        else: 
            print("Invalid option. Please make another selection.")


run_app()           





