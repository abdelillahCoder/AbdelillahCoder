def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, (task, completed) in enumerate(tasks, start=1):
            status = "✔" if completed else "✘"
            print(f"{i}. {task} [{status}]")

def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append((task, False))
    print(f"Task '{task}' added!")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("\nEnter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task[0]}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_completed(tasks):
    view_tasks(tasks)
    try:
        index = int(input("\nEnter the task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            task, _ = tasks[index]
            tasks[index] = (task, True)
            print(f"Task '{task}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_completed(tasks)
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
