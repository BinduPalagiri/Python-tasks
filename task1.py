class Task:
    def __init__(self, title, priority, due_date, completed=False):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        return f"{self.title} - Priority: {self.priority}, Due Date: {self.due_date}, Completed: {self.completed}"
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_title):
        self.tasks = [task for task in self.tasks if task.title != task_title]

    def mark_task_as_completed(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.completed = True

    def get_tasks(self):
        return self.tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    task_manager = TaskManager()
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title, priority, due_date)
            task_manager.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            title = input("Enter task title to remove: ")
            task_manager.remove_task(title)
            print("Task removed successfully.")
        elif choice == "3":
            title = input("Enter task title to mark as completed: ")
            task_manager.mark_task_as_completed(title)
            print("Task marked as completed.")
        elif choice == "4":
            tasks = task_manager.get_tasks()
            display_tasks(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
