import json
import os

TODO_FILE = "todo_list.json"

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print("Task added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
        for idx, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. [{status}] {task['task']}")

    def mark_complete(self, index):
        try:
            self.tasks[index - 1]["completed"] = True
            self.save_tasks()
            print("Task marked as complete!")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"Deleted: {removed['task']}")
        except IndexError:
            print("Invalid task number.")

    def save_tasks(self):
        with open(TODO_FILE, "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, "r") as f:
                self.tasks = json.load(f)

def menu():
    todo = ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            todo.view_tasks()
        elif choice == "2":
            task = input("Enter your task: ")
            todo.add_task(task)
        elif choice == "3":
            todo.view_tasks()
            index = int(input("Enter task number to mark complete: "))
            todo.mark_complete(index)
        elif choice == "4":
            todo.view_tasks()
            index = int(input("Enter task number to delete: "))
            todo.delete_task(index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()