def main():
    print("=== Task Manager ===")
    tasks = []

    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            print("Task added!")
        elif choice == "2":
            if not tasks:
                print("No tasks yet.")
            else:
                print("Your tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
