import json

def initialize_tasks_file():
    """Create initial tasks.json file with a sample completed task."""
    initial_task = {
        "id": 1,
        "description": "Create tasks.json",
        "category": "System",
        "due_date": "2025-12-31",
        "completed": True
    }
    
    with open("tasks.json", "w") as file:
        json.dump([initial_task], file, indent=4)
        print("Created tasks.json with initial task")

class Task:

    def __init__(self, id, description, category = "Default", due_date = "2025-12-31", completed=False):
        self.id = id
        self.description = description
        self.completed = completed
        self.category = category
        self.due_date = due_date

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] #{self.id} ({self.category}): {self.description} Due by: {self.due_date}"
    
class TaskManager:

    FILENAME = "tasks.json"

    def __init__(self):
        self._tasks = []
        self._next_id = 1
        self.load_tasks()

    def add_task(self, description, category="Default", due_date = "2025-12-31"):
        task = Task(self._next_id, description, category, due_date)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Task added: {description}")
        self.save_tasks()

    def list_tasks(self):
        if not self._tasks:
            print("No pending tasks")
        else:
            for task in self._tasks:
                print(task)

    def complete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"Task completed: {task}")
                self.save_tasks()
                return
        print(f"Task not found: #{id}")

    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Task deleted: #{id}")
                self.save_tasks()
                return
        print(f"Task not found: #{id}")

    def load_tasks(self, retry_count=0):
        """Load tasks from JSON file with retry mechanism."""
        MAX_RETRIES = 3
        try:
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
                # Use get() to provide defaults if keys are missing (backwards compatibility)
                self._tasks = [
                    Task(
                        item.get("id"),
                        item.get("description", ""),
                        item.get("category", "Default"),
                        item.get("due_date", "2025-12-31"),
                        item.get("completed", False)
                    ) for item in data
                ]
                if self._tasks:
                    self._next_id = self._tasks[-1].id + 1
                else:
                    self._next_id = 1

        except FileNotFoundError:
            if retry_count >= MAX_RETRIES:
                print(f"Error: Could not load tasks after {MAX_RETRIES} attempts")
                return
            print(f"Retrying... Attempt {retry_count + 1}/{MAX_RETRIES}")
            initialize_tasks_file()             # Create file with initial task
            self.load_tasks(retry_count + 1)    # Retry loading

    def save_tasks(self):
        with open(self.FILENAME, "w") as file:
            json.dump([
                {
                    "id": task.id,
                    "description": task.description,
                    "category": task.category,
                    "due_date": task.due_date,
                    "completed": task.completed
                } for task in self._tasks
            ], file, indent=4)