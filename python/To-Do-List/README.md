# To-Do LIST APPLICATION

This simple To-Do List application is built using Python and the Tkinter library. It provides a simple graphical user interface for users to add, remove, and view tasks in a to-do list.

## Features

- **Add Task:** Users can input tasks using the entry field and click the "ADD" button to add them to the to-do list.
- **Remove Task:** Tasks can be removed from the list by selecting them and clicking the "Remove Task" button.
- **Persistence:** The to-do list is saved to a text file (`tasklist.txt`), allowing users to retrieve their tasks even after closing the application.

## Getting Started

### Prerequisites

- Python installed on your system (version 3.x recommended).

### Installation

1. Clone or download the repository to your local machine.

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. Navigate to the project directory.

   ```bash
   cd your-repository
   ```

3. Install the required dependencies.

   ```bash
   # Install Tkinter (if not already installed)
   pip install tk
   ```

### Usage

1. Run the application.

   ```bash
   python your_script_name.py
   ```

2. The application window will appear, providing an interface to interact with the to-do list.

## Usage Example

1. Enter a task in the input field.
2. Click the "ADD" button to add the task to the list.
3. To remove a task, select it from the list and click the "Remove Task" button.

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new pull request.

## Acknowledgments

- The project was inspired by the need for a simple do to list application thats easy to use.
- Special thanks to the Tkinter library for providing the GUI framework.

Feel free to customize, enhance, and use this project to suit your needs. Happy task managing!

# HOW THE PROJECT WORKS

This To-Do List application is built using Python and the Tkinter library. It provides a graphical user interface for users to manage their tasks efficiently.

## Architecture

The application uses the Tkinter library for creating a GUI. Here's an overview of its components:

- **Main Window (`root`):** The primary window where the entire application resides. It includes the to-do list, input fields, and buttons.

- **To-Do List (`listbox`):** A Tkinter Listbox widget to display the tasks. The list is populated from a text file (`tasklist.txt`) for persistence across sessions.

- **Input Field (`task_entry`):** An Entry widget for users to input new tasks.

- **Buttons (`ADD` and `Remove Task`):** Buttons to add a new task and remove a selected task, respectively.

## Workflow

1. **Adding a Task:**

   - Users input a task in the `task_entry` field.
   - Clicking the "ADD" button triggers the `addTask` function.
   - The new task is appended to the `task_list` and displayed in the `listbox`.
   - The task is also saved to the `tasklist.txt` file for persistence.

2. **Removing a Task:**

   - Users select a task from the `listbox`.
   - Clicking the "Remove Task" button triggers the `deleteTask` function.
   - The selected task is removed from both the `task_list` and the `listbox`.
   - The updated task list is saved to the `tasklist.txt` file.

3. **File Operations:**
   - The `openTaskFile` function reads the contents of the `tasklist.txt` file during application startup.
   - If the file does not exist, it is created.

## File Structure

- **`gui.py`:** The main Python script containing the application logic.
- **`tasklist.txt`:** A text file to store the tasks persistently.

## Contribution

Feel free to contribute to the project by following these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new pull request.

# Happy coding
