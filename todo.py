import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"
tasks = []

def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
    print("Tasks saved.")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append({
            "task": task,
            "done": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"Task added: {task}")
        save_tasks()
    else:
        print("Task cannot be empty.")

def list_tasks():
    if not tasks:
        print("No tasks added yet.")
        return
    print("\nYour Tasks:")
    print("-" * 40)
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        print(f"{i + 1}. {task['task']} [{status}] (Added: {task['created_at']})")
    print("-" * 40)

def toggle_done():
    list_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to toggle status: "))
        task = tasks[task_num - 1]
        task["done"] = not task["done"]
        print(f"Task {task_num} status changed to {'done' if task['done'] else 'not done'}.")
        save_tasks()
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task():
    list_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to delete: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Task deleted: {removed_task['task']}")
        save_tasks()
    except (ValueError, IndexError):
        print("Invalid task number.")

def show_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Toggle Task Status")
    print("4. Delete Task")
    print("5. Exit")

def main():
    load_tasks()
    print("Welcome to the To-Do List Application")
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            toggle_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
