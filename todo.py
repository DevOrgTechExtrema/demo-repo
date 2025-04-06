import json

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    print("Tasks saved.")
    
tasks = []

def add_task():
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
    print("6. Change Task")
    
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

def put_task():
    task_index = int(input("Enter the number of the task to change: "))
    task = input("Enter the new task: ").strip()
    if task:
        tasks[task_index - 1] = {"task": task, "done": False}
        print(f"Task changed: {task}")
    else:
        print("Task cannot be empty.")
        
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
        elif choice == "6":
            put_task()

if __name__ == "__main__":
    main()
