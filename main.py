from task_manager import TaskManager, initialize_tasks_file
from ai_service import create_simple_tasks
from datetime import datetime
import os

def print_menu(): 
    print("\n--- Smart Task Manager ---")
    print("1. Add task")
    print("2. Add complex task (with AI)")
    print("3. List tasks")
    print("4. Complete task")
    print("5. Delete task")
    print("6. Exit")

def get_date_input():
    for _ in range(2):
        user_input = input("Enter a date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(user_input, "%Y-%m-%d")
            return user_input
        except ValueError:
            print("Invalid format. Please use YYYY-MM-DD.")
    return "2020-12-31"

def handle_choice(choice: int, manager: TaskManager) -> bool:
    """Handle menu choice and return False if program should exit."""
    try:
        match choice:
            case 1:
                description = input("Task description: ")
                category = input("Task category (optional): ")
                due_date = get_date_input()
                if due_date.strip() == "":
                    due_date = "2025-12-31"
                manager.add_task(description, category, due_date)             
            case 2:
                description = input("Complex task description: ")
                subtasks = create_simple_tasks(description)
                for subtask in subtasks:
                    if not subtask.startswith("Error:"):
                        manager.add_task(subtask)
                    else:
                        print(subtask)
                        break
            case 3:
                manager.list_tasks()
            case 4:
                id = int(input("ID of the task to complete: "))
                manager.complete_task(id)
            case 5:
                id = int(input("ID of the task to delete: "))
                manager.delete_task(id)
            case 6:
                print("Exiting...")
                return False                
            case _:
                print("Invalid option. Please choose another.")
        
        return True
            
    except ValueError:
        print("Invalid option. Please choose another.")
        return True

def main():
    manager = TaskManager()
    while True:
        print_menu()
        try:
            choice = int(input("Choose an option: "))
            if not handle_choice(choice, manager):
                break
        except ValueError:
            print("Invalid option. Please choose another.")

if __name__ == "__main__":
    if not os.path.exists("tasks.json"):
        initialize_tasks_file()
    main()