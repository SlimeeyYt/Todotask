# To-Do List Manager

A simple, console-based Python application for managing your daily tasks. This lightweight project allows you to add, remove, update, and view tasks, with all data stored persistently in a local JSON file.

## ✅ Features
➕ Add Tasks

Create new tasks and optionally assign a due date.

🗑 Remove Tasks

Delete tasks that are no longer needed.

✔ Mark Tasks as Completed

Update a task’s status to Completed.

📄 View All Tasks

Displays a list of all tasks, including:

Task Name

Status (Pending / Completed)

Due Date (optional)

Timestamp (when the task was added)

💾 Persistent Storage

Tasks are saved in a tasks.json file so your data remains intact between sessions.

## ▶️ How to Use
1. Clone the repository:
```
git clone <https://github.com/SlimeeyYt/Todotask>
cd todo-list-manager
```

2. Run the Python script:
```
python todo_list.py
```

3. Use the interactive menu:

| Option | Description              |
| ------ | ------------------------ |
| **1**  | Add a new task           |
| **2**  | Remove a task            |
| **3**  | Mark a task as completed |
| **4**  | View all tasks           |
| **5**  | Exit the application     |

## 📦 Requirements

Python 3.6 or later

No external libraries required (only uses Python's standard library)


## 📁 Files

todo_list.py – Main application logic

tasks.json – Stores all task data persistently

