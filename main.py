tasks = []

def add_task(title):
    tasks.append({"title": title, "done": False})

def list_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else " "
        print(f"{i+1}. [{status}] {task['title']}")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def main():
    while True:
        print("\n1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Task title: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            idx = int(input("Task number: ")) - 1
            complete_task(idx)
        elif choice == "4":
            idx = int(input("Task number: ")) - 1
            delete_task(idx)
        elif choice == "0":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
