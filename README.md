To-Do List Manager
A simple, console-based Python application for managing tasks. This project allows you to create, manage, and track your daily tasks with ease. It uses a JSON file for persistent storage so your tasks are saved between sessions.

Features
Add Tasks: Create new tasks and optionally assign a due date.
Remove Tasks: Delete tasks from the list when no longer needed.
Mark Tasks as Completed: Update the status of a task to "Completed."
View Tasks: List all tasks with their details, including:
Task Name
Status (Pending/Completed)
Due Date (if assigned)
Timestamp of when the task was added
Persistent Storage: All tasks are saved in a tasks.json file, ensuring data is not lost when the application is closed.
How to Use
Clone this repository:

cd todo-list-manager
Run the Python script:

python todo_list.py
Interact with the application using the menu options:

Option 1: Add a new task.
Option 2: Remove a task.
Option 3: Mark a task as completed.
Option 4: List all tasks.
Option 5: Exit the application.
Requirements
Python 3.6 or later
No external dependencies (uses Python's standard library)
File Structure
todo_list.py: Main Python script for the application.
tasks.json: JSON file for storing tasks (created automatically when the script is run).
Example Workflow
Add a task:

mathematica
Copy code
Enter the task name: Buy groceries
Enter due date (YYYY-MM-DD): 2024-11-20
View tasks:



1. Task: Buy groceries
   Status: Pending
   Due: 2024-11-20
   Added on: 2024-11-15 10:15:00
Mark a task as completed:


Enter task number to mark as completed: 1
View updated tasks:


1. Task: Buy groceries
   Status: Completed
   Due: 2024-11-20
   Added on: 2024-11-15 10:15:00
Future Enhancements
Add priority levels for tasks.
Include task categorization (work, personal, etc.).
Support editing existing tasks.
Create a GUI version of the application.
