import json
import os
from datetime import datetime

def get_last_modified_timestamp(file_path):
    """
    Returns the last modified timestamp of a file as a formatted string.
    
    Args:
        file_path: Path to the file.
    
    Returns:
        A string representing the last modified timestamp in "YYYY-MM-DD HH:MM:SS" format,
        or None if the file does not exist.
    """
    try:
        timestamp = os.path.getmtime(file_path)
        return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
    except FileNotFoundError:
        return False
    
def load_tasks():
    """
    Loads tasks from the "tasks.json" file with error handling.
    
    If the file does not exist or contains invalid JSON, prints an error message. After loading, prints the last modified timestamp if available.
    
    Returns:
        The list of tasks loaded from the file, or an empty list if loading fails.
    """
    file_path = "tasks.json"
    try:
        with open(file_path, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error reading the JSON file.")
        
    last_modified = get_last_modified_timestamp(file_path)
    if last_modified:
        print(f"Tasks loaded. Last modified on: {last_modified}")
    return tasks


tasks = load_tasks()

def save_tasks():
    """
    Saves the current list of tasks to the "tasks.json" file in JSON format.
    """
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    print("Tasks saved.")    

def add_task():
    """
    Prompts the user to add a new task to the to-do list.
    
    If the input is non-empty, adds the task with a status of not done. Prints an error
    message if the input is empty.
    """
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print(f"Task added: {task}")
    else:
        print("Task cannot be empty.")
    
def show_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    
def list_tasks():
    if not tasks:
        print("No tasks added yet.")
        return
    print("\nYour Tasks:")
    print("-" * 20)
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        print(f"{i + 1}. {task['task']} [{status}]")
    print("-" * 20)
     
def mark_done():
    list_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to mark as done: "))
        tasks[task_num - 1]["done"] = True
        print(f"Task {task_num} marked as done.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task():
    list_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to delete: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Task {task_num} deleted: {removed_task['task']}")
    except (ValueError, IndexError):
        print("Invalid task number.")
        
def main():
    print("Welcome to the To-Do List Application")
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
