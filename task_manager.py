import json

def initialize_tasks_file():
    """Create initial tasks.json file with a sample completed task."""
    initial_task = {
        "id": 1,
        "description": "Create tasks.json",
        "completed": True
    }
    
    with open("tasks.json", "w") as file:
        json.dump([initial_task], file, indent=4)
        print("Created tasks.json with initial task")

class Task:

    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"
    
class TaskManager:

    FILENAME = "tasks.json"

    def __init__(self):
        self._tasks = []
        self._next_id = 1
        self.load_tasks()

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Tarea añadida: {description}")
        self.save_tasks()

    def list_tasks(self):
        if not self._tasks:
            print("No hay tareas pendientes")
        else:
            for task in self._tasks:
                print(task)

    def complete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"Tarea completada: {task}")
                self.save_tasks()
                return
        print(f"Tarea no encontrada: #{id}")

    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Tarea eliminada: #{id}")
                self.save_tasks()
                return
        print(f"Tarea no encontrada: #{id}")

    def load_tasks(self, retry_count=0):
        """Load tasks from JSON file with retry mechanism."""
        MAX_RETRIES = 3
        try:
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
                self._tasks = [Task(item["id"], item["description"], item["completed"]) for item in data]
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
            json.dump([{"id": task.id, "description": task.description, "completed": task.completed} for task in self._tasks], file, indent=4)