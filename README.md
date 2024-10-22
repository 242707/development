Task Manager CLI Application

Project Description

The Task Manager is a simple command-line interface (CLI) application that allows users to manage their daily tasks. Users can add, view, delete, and mark tasks as complete. The tasks are saved in a JSON file (tasks.json) and loaded automatically when the application starts.

The primary goal of this project is to provide users with an easy-to-use tool for task management through the terminal.


Instructions for Running the Application:
Prerequisites:
Python 3.x installed on your system.

Steps to Run:
Clone or Download the Project:

Navigate to the directory where you'd like to store the project.
Clone the repository or download the project files.

Navigate to Project Directory: task_manager

Run the Application: Execute the following command to start the Task Manager:task_manager.py

Use the CLI: Once the application is running, you will be presented with a menu of options:

Task Manager
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save Tasks
6. Exit
Choose an option by entering the corresponding number (1-6).
Follow the prompts to interact with the Task Manager (e.g., inputting task titles or task IDs).
Exiting:

Before exiting the application (Option 6), ensure that tasks are saved by selecting the Save Tasks option (Option 5).
The tasks are automatically saved when the application exits, ensuring no data is lost.

Overview of Functionalities

Add a Task:
Adds a new task with a unique ID.
Tasks have a title and a completion status (default is "Not Completed").


View Tasks:
Displays a list of all tasks along with their IDs and completion status.
Format: [Task_ID] Task_Title - Status.


Delete a Task:
Removes a task by entering its ID.
The user is prompted to input the task ID to delete.


Mark Task as Complete:
Marks a task as completed by its ID.
Tasks that are already completed cannot be marked again.


Save Tasks:
Saves the current task list to a JSON file (tasks.json).
Data is persisted across application runs.


Load Tasks:
Automatically loads tasks from the tasks.json file when the application starts.
If no file exists, the application starts with an empty task list.
