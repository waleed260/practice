import sys

def display_menu():
    """Displays the interactive menu options."""
    print("\n--- Task Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print("--------------------")

def view_tasks(tasks):
    """Lists all current tasks with their indices."""
    if not tasks:
        print("\n[!] Your task list is empty.")
    else:
        print("\n--- Your Tasks ---")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    """Prompts for a task description and adds it to the list."""
    description = input("\nEnter task description: ").strip()
    if description:
        tasks.append(description)
        print(f"[+] Task '{description}' added.")
    else:
        print("[!] Task description cannot be empty.")

def remove_task(tasks):
    """Removes a task by its index."""
    if not tasks:
        print("\n[!] Nothing to remove.")
        return

    view_tasks(tasks)
    try:
        choice = int(input("\nEnter the task number to remove: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"[-] Task '{removed}' removed.")
        else:
            print("[!] Invalid task number.")
    except ValueError:
        print("[!] Please enter a valid number.")

def main():
    """Main program loop."""
    tasks = []
    print("Welcome to your Python Practice Task Manager!")
    
    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("[!] Invalid selection. Please choose 1-4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Goodbye!")
        sys.exit(0)
