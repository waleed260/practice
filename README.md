# Practice - Python Task Manager

A simple command-line Task Manager application built in Python.

## Features

- **View Tasks**: List all current tasks with their indices
- **Add Task**: Add new tasks with custom descriptions
- **Remove Task**: Delete tasks by their index number
- **Interactive Menu**: User-friendly CLI interface

## Requirements

- Python 3.12 or higher

## Installation

This project uses `uv` as the build system. To install:

```bash
# Clone the repository
git clone <repository-url>
cd practice

# Install using uv
uv pip install -e .
```

## Usage

Run the application directly:

```bash
python prac.py
```

Or use the installed package command:

```bash
practice
```

### Menu Options

```
--- Task Manager ---
1. View Tasks
2. Add Task
3. Remove Task
4. Exit
--------------------
```

## Project Structure

```
practice/
├── prac.py              # Main application script
├── pyproject.toml       # Project configuration
├── README.md            # This file
└── src/
    └── practice/
        └── __init__.py  # Package entry point
```

## License
