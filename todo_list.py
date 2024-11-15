import os
import json
import time
import sys
from datetime import datetime

# Utilities
def clear_screen():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

def print_divider():
    print('-' * 50)

# Task Class
class Task:
    def __init__(self, task_name, due_date=None):
        self.task_name = task_name
        self.completed = False
        self.due_date = due_date
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def mark_completed(self):
        self.completed = True
        
    def __str__(self):
        status = 'Completed' if self.completed else 'Pending'
        return f"Task: {self.task_name}\nStatus: {status}\nDue: {self.due_date if self.due_date else 'No Due Date'}\nAdded on: {self.timestamp}\n"

# Task Manager Class
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
    
    def add_task(self, task_name, due_date=None):
        task = Task(task_name, due_date)
        self.tasks.append(task)
        self.save_tasks()
    
    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
            self.save_tasks()
    
    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
            self.save_tasks()
    
    def list_tasks(self):
        if not self.tasks:
            print("No tasks available!")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")
    
    def load_tasks(self):
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as file:
                try:
                    self.tasks = [Task(**task) for task in json.load(file)]
                except json.JSONDecodeError:
                    self.tasks = []
    
    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file, indent=4)

# Task Management Menu
def display_menu():
    print_divider()
    print("To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task Completed")
    print("4. List Tasks")
    print("5. Exit")
    print_divider()

def get_user_choice():
    try:
        choice = int(input("Please choose an option: "))
        return choice
    except ValueError:
        return -1

def task_manager_loop():
    task_manager = TaskManager()
    while True:
        display_menu()
        choice = get_user_choice()
        clear_screen()
        if choice == 1:
            task_name = input("Enter the task name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task_manager.add_task(task_name, due_date)
        elif choice == 2:
            task_manager.list_tasks()
            try:
                task_index = int(input("Enter task number to remove: ")) - 1
                task_manager.remove_task(task_index)
            except ValueError:
                print("Invalid input!")
        elif choice == 3:
            task_manager.list_tasks()
            try:
                task_index = int(input("Enter task number to mark as completed: ")) - 1
                task_manager.mark_task_completed(task_index)
            except ValueError:
                print("Invalid input!")
        elif choice == 4:
            task_manager.list_tasks()
        elif choice == 5:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again!")
        time.sleep(2)
        clear_screen()

if __name__ == "__main__":
    task_manager_loop()
