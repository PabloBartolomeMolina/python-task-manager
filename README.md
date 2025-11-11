# TaskManager 📝

A smart task manager developed in Python that allows creating, managing and completing tasks efficiently. It includes AI integration to decompose complex tasks into simpler, actionable subtasks.

## 📁 Estructura del proyecto
```
TaskManager/
├── main.py               # Entry point with menu interface and option handling
├── task_manager.py       # Core logic and file operations
├── ai_service.py         # OpenAI integration
├── test_task_manager.py  # Unit test suite
├── .env                  # Environment variables (not in git)
├── requirements.txt      # Project dependencies
├── tasks.json            # Personal data file (not in git)
├── example_tasks.json    # Example template
├── .gitignore            # Git configuration
└── README.md             # Project documentation
```

### Ignored files
The following files are excluded from version control:

- `tasks.json`: Local data file
- `.venv/`: Python virtual environment
- `__pycache__/`: Compiled Python files
- `.env`: Environment variables

## 💾 Data storage

Las tareas se almacenan localmente en `tasks.json`. This file:
- Is created automatically on first run
- Contains your personal task list
- Is not included in version control
- Uses this structure:

```json
[
    {
        "id": 1,
        "description": "Create tasks.json",
        "completed": true
    }
]
```

## 🚀 Main features

- Task management: create, list, complete and delete tasks from the CLI  
- Persistence: automatic JSON storage with a safe retry mechanism (max 3 attempts)  
- Categories: tasks include an optional category field for better organization  
- AI integration: optional OpenAI-based decomposition of complex tasks into subtasks  
- Input validation and graceful error handling for a robust CLI experience  
- Type hints and modular design for maintainability and easier testing

## 🛡️ Error handling

The application implements several safeguards:

- Retry mechanism for file operations (up to 3 attempts) to handle transient I/O issues  
- Backwards compatibility when loading older JSON files (missing keys are handled with defaults)  
- Validation of user input in the menu and for numeric IDs  
- Graceful messages and controlled exits when unrecoverable errors occur

## 🛠️ Technologies used

- Python 3.13+  
- OpenAI API (optional) for AI features  
- JSON for local persistence  
- unittest for unit tests  
- python-dotenv for environment variables

## 🎮 Running the program

Run the CLI application:

```bash
python main.py
```

On first run, the app will create `tasks.json` if it does not exist and seed it with a single completed system task.

### Main menu

1. **Add task** — Create a new task (you can specify a category)  
2. **Add complex task (with AI)** — Use AI to decompose a complex task into subtasks  
3. **List tasks** — Show all tasks with status, id and category  
4. **Complete task** — Mark a task as completed by id  
5. **Delete task** — Remove a task by id  
6. **Exit** — Quit the application

### Examples of use

#### Add a simple task
```
Choose an option: 1
Task description: Buy milk
Task added: Buy milk
```

#### Add a complex task with AI
```
Choose an option: 2
Complex task description: Organize a birthday party
```
The AI will decompose this task into subtasks such as:
- Make a guest list
- Book a venue
- Plan the menu and buy food
- Decorate the space
- Coordinate activities and entertainment

## 🧪 Tests

### Run the unit tests:

```bash
python -m unittest test_task_manager.py -v
```

### Test coverage

Tests cover:
- ✅ Adding tasks
- ✅ Deleting existing tasks
- ✅ Handling non-existent tasks
- ✅ Listing tasks
- ✅ Completing tasks

## 🤖 Funcionalidad de IA

The OpenAI integration enables:

- Decomposing a single complex task into 3–5 actionable subtasks  
- Returning useful suggestions to add as individual tasks automatically  
- Failing gracefully when the API is not available or the key is missing

## 🔒 Security

- API keys and sensitive configuration are loaded from environment variables (`.env`)  
- No credentials are stored in source code or tracked by Git  
- Errors from external services are handled to avoid leaking sensitive information

## 🚧 Known limitations

- AI functionality requires internet access and a valid API key  
- Tasks are stored as plain JSON (no encryption)  
- No automatic backup or synchronization features

## 🤝 Contributions

Contributions are welcome. Typical workflow:

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/name`)  
3. Commit your changes (`git commit -m "feat: ..."` )  
4. Push and open a Pull Request

Please follow the existing code style and add tests for new functionality.

## 📋 Roadmap

Planned improvements:

- [ ] GUI client for easier interaction
- [x] Tasks categories
- [ ] Due dates and reminders
- [ ] Calls to action
- [ ] Export/import and backup options
- [ ] Advanced filtering and search
- [ ] Productivity statistics and reports

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 👨‍💻 Author

Base developed by [MoureDev](https://github.com/mouredev)  
Improvements by [Pablo](https://github.com/PabloBartolomeMolina)

## 📞 Support

If you find an issue or have suggestions, open an issue on GitHub or contact the maintainer via LinkedIn.
- [issue](https://github.com/PabloBartolomeMolina/python-task-manager/issues)
- [Linkedin](https://www.linkedin.com/in/pablo-bartolome-molina/)
---

*Proyecto desarrollado con 💙 en Python*