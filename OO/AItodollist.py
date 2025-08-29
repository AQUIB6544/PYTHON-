import json
import os

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks found!")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task["done"] else "❌"
            print(f"{i}. {task['title']} [{status}]")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter task: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            num = int(input("Enter task number to mark done: "))
            if 0 < num <= len(tasks):
                tasks[num-1]["done"] = True
                save_tasks(tasks)
        elif choice == "4":
            show_tasks(tasks)
            num = int(input("Enter task number to edit: "))
            if 0 < num <= len(tasks):
                new_title = input("Enter new task name: ")
                tasks[num-1]["title"] = new_title
                save_tasks(tasks)
        elif choice == "5":
            show_tasks(tasks)
            num = int(input("Enter task number to delete: "))
            if 0 < num <= len(tasks):
                tasks.pop(num-1)
                save_tasks(tasks)
        elif choice == "6":
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()