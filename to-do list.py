def menu():
    print("\n--- To-Do List Menu ---")
    print("1. View my To-Do List")
    print("2. Add New Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nTo-Do List:")
        index = 1
        for task in tasks:
            status = "Done" if task["completed"] else "Not Done"
            print(f"{index}. {task['task']} - {status}")
            index += 1

def add_task(tasks):
    task_description = input("\nEnter the task description: ")
    tasks += [{"task": task_description, "completed": False}]
    print("Task added successfully.")

def task_completed(tasks):
    view_tasks(tasks)
    task_no = int(input("\nEnter the task number to mark as completed: "))
    if 0 < task_no <= len(tasks):
        tasks[task_no - 1]["completed"] = True
        print("Task is completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_no = int(input("\nEnter the task number to delete: "))
    if 0 < task_no <= len(tasks):
        deleted_task = tasks[task_no - 1]
        del tasks[task_no - 1]
        print(f"Task '{deleted_task['task']}' deleted.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        menu()
        choice = input("\nChoose an option: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
