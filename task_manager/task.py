import json
import os


class Task:
    """Represents a task with a unique task ID, title, and completion status."""

    def __init__(self, task_id, title):
        self.task_id = task_id
        self.title = title
        self.completed = False

    def __repr__(self):
        return f"Task(task_id={self.task_id}, title='{self.title}', completed={self.completed})"


class TaskManager:
    """Manages a list of tasks."""

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title):
        """Add a new task with a unique ID."""
        if any(task.title == title for task in self.tasks):
            print(f"Task with title '{title}' already exists.")
            return

        task_id = max([task.task_id for task in self.tasks], default=0) + 1
        new_task = Task(task_id, title)
        self.tasks.append(new_task)
        print(f"Task added: {new_task}")

    def view_tasks(self):
        """Display all tasks and their completion status."""
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            status = "Completed" if task.completed else "Not Completed"
            print(f"[{task.task_id}] {task.title} - {status}")

    def delete_task(self, task_id):
        """Remove a task by its ID."""
        try:
            for task in self.tasks:
                if task.task_id == task_id:
                    self.tasks.remove(task)
                    print(f"Task deleted: {task}")
                    return
            print(f"Task with ID {task_id} not found.")
        except Exception as e:
            print(f"Error deleting task: {e}")

    def mark_task_as_complete(self, task_id):
        """Mark a task as completed."""
        try:
            for task in self.tasks:
                if task.task_id == task_id:
                    if task.completed:
                        print(f"Task with ID {task_id} is already completed.")
                    else:
                        task.completed = True
                        print(f"Task marked as complete: {task}")
                    return
            print(f"Task with ID {task_id} not found.")
        except Exception as e:
            print(f"Error marking task as complete: {e}")

    def save_tasks(self):
        """Save the list of tasks to a JSON file."""
        try:
            with open('tasks.json', 'w') as file:
                json.dump([{
                    'task_id': task.task_id,
                    'title': task.title,
                    'completed': task.completed
                } for task in self.tasks], file, indent=4)
            print("Tasks saved to tasks.json.")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        """Load tasks from a JSON file."""
        if os.path.exists('tasks.json'):
            try:
                with open('tasks.json', 'r') as file:
                    tasks_data = json.load(file)
                    for data in tasks_data:
                        try:
                            task_id = data.get('task_id')
                            title = data.get('title')
                            completed = data.get('completed', False)
                            task = Task(task_id, title)
                            task.completed = completed
                            self.tasks.append(task)
                        except Exception as e:
                            print(f"Error loading task data: {e}")
                print("Tasks loaded from tasks.json.")
            except json.JSONDecodeError:
                print("Error reading JSON data. The file may be corrupted.")
            except Exception as e:
                print(f"Error loading tasks: {e}")
        else:
            print("No existing task file found. Starting with an empty task list.")


def main():
    """Main function to run the task manager CLI."""
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        try:
            if choice == '1':
                title = input("Enter task title: ")
                task_manager.add_task(title)
            elif choice == '2':
                task_manager.view_tasks()
            elif choice == '3':
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            elif choice == '4':
                task_id = int(input("Enter task ID to mark as complete: "))
                task_manager.mark_task_as_complete(task_id)
            elif choice == '5':
                task_manager.save_tasks()
            elif choice == '6':
                task_manager.save_tasks()
                print("Exiting Task Manager.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
