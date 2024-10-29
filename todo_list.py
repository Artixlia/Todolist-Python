def display_menu():
    print("\nWelcome to your To-Do List Program!")
    print("Menu:")
    print("1. Add a new task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Delete a completed task")
    print("5. Exit")

def add_task(tasks):
    task_description = input("Enter the task description: ")
    tasks[task_description] = "Pending"
    print(f"Task '{task_description}' has been added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for i, (task, status) in enumerate(tasks.items(), 1):
            print(f"{i}. {task} ({status})")

def mark_task_completed(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to mark as completed: "))
            task_list = list(tasks.keys())
            task_to_mark = task_list[task_number - 1]
            tasks[task_to_mark] = "Completed"
            print(f"Task '{task_to_mark}' has been marked as completed.")
        except (IndexError, ValueError):
            print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to delete: "))
            task_list = list(tasks.keys())
            task_to_delete = task_list[task_number - 1]
            if tasks[task_to_delete] == "Completed":
                del tasks[task_to_delete]
                print(f"Task '{task_to_delete}' has been deleted.")
            else:
                print("Only completed tasks can be deleted.")
        except (IndexError, ValueError):
            print("Invalid task number.")

def main():
    tasks = {}
    while True:
        display_menu()
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                mark_task_completed(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Please choose a valid option.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
