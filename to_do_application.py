tasks = []


print("\n--- TO-DO LIST ---")
print("1. Add Task")
print("2. View Tasks")
print("3. Remove Task")
print("4. Exit")
while True:
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_number = int(input("Enter task number to remove: "))

            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Removed: {removed_task}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")