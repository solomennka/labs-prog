import os
os.system("chcp 65001 > nul")


def show_processes():
    """
    Function that shows all running processes.
    @return: None
    """
    os.system("tasklist")


def process_info(pid: int):
    """
    Function that shows process info by PID.
    @param pid: int - process id
    @return: None
    """
    os.system(f'tasklist /FI "PID eq {pid}"')


def kill_process(pid: int):
    """
    Function that kills process by PID.
    @param pid: int - process id
    @return: None
    """
    os.system(f"taskkill /PID {pid} /F")
    print("Process killed")


def env_show():
    """
    Function that shows environment variables.
    @return: None
    """
    for k, v in os.environ.items():
        print(f"{k}={v}")


def env_add(key: str, value: str):
    """
    Function that adds environment variable.
    @param key: str
    @param value: str
    @return: None
    """
    os.environ[key] = value
    print("Variable added")


def change_priority(pid: int, priority: int):
    """
    Function that changes process priority.
    @param pid: int
    @param priority: int
    @return: None
    """
    try:
        os.system(f'wmic process where processid={pid} CALL setpriority {priority}')
        print("Priority changed")
    except PermissionError:
        print("Error: no permission")
    except Exception as e:
        print("Error:", e)


def system_info():
    """
    Function that shows system info.
    @return: None
    """
    try:
        print("System:", os.name)
        print("Computer:", os.getenv("COMPUTERNAME"))
        print("User:", os.getenv("USERNAME"))
    except AttributeError:
        print("Error: system info unavailable")


def menu():
    """
    Main menu function.
    @return: None
    """
    while True:
        print("\nMenu:")
        print("a) Show processes")
        print("b) Process info")
        print("c) Kill process")
        print("d) Env variables")
        print("e) Change priority")
        print("f) System info")
        print("g) Exit")

        choice = input("Choose option: ")

        if choice == "a":
            show_processes()

        elif choice == "b":
            try:
                pid = int(input("Enter PID: "))
                process_info(pid)
            except ValueError:
                print("Invalid PID")

        elif choice == "c":
            try:
                pid = int(input("Enter PID: "))
                kill_process(pid)
            except ValueError:
                print("Invalid PID")

        elif choice == "d":
            env_show()
            add = input("Add new variable? (y/n): ")
            if add == "y":
                key = input("Enter key: ")
                value = input("Enter value: ")
                env_add(key, value)

        elif choice == "e":
            try:
                pid = int(input("Enter PID: "))
                pr = int(input("Enter priority: "))
                change_priority(pid, pr)
            except ValueError:
                print("Invalid input")

        elif choice == "f":
            system_info()

        elif choice == "g":
            print("Exit")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()