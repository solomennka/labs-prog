import os


def copy_file(src: str, dst: str):
    """
    Function that copies file in binary mode.
    @param src: str - source file
    @param dst: str - destination file
    @return: None
    """
    with open(src, "rb") as s, open(dst, "wb") as d:
        d.write(s.read())


def move_file(src: str, dst: str):
    """
    Function that moves or renames file.
    @param src: str - source path
    @param dst: str - destination path
    @return: None
    """
    os.replace(src, dst)


def make_dirs(path: str):
    """
    Function that creates directories.
    @param path: str - directory path
    @return: None
    """
    os.makedirs(path, exist_ok=True)


def make_empty_file(name: str):
    """
    Function that creates empty file.
    @param name: str - file name
    @return: None
    """
    with open(name, 'w') as f:
        f.write("")


def make_many_files(n: int):
    """
    Function that creates many files.
    @param n: int - number of files
    @return: None
    """
    for i in range(n):
        with open(f"file_{i}.txt", "w") as f:
            f.write("")


def show_dir(path: str):
    """
    Function that prints directory content.
    @param path: str - directory path
    @return: None
    """
    print("Contents of the script folder:\n" + '\n'.join(os.listdir()))


def show_dir_custom(path: str):
    """
    Function that prints specific directory content.
    @param path: str - directory path
    @return: None
    """
    print()
    print(f"Contents of the folder {path}:\n" + '\n'.join(os.listdir()))
    print()


def go_to(path: str):
    """
    Function that changes directory.
    @param path: str - path
    @return: None
    """
    os.chdir(path)


def make_and_del_dir(name: str):
    """
    Function that creates and deletes directory.
    @param name: str - directory name
    @return: None
    """
    os.mkdir(name)
    os.rmdir(name)


def make_structure():
    """
    Function that creates directory structure.
    @return: None
    """
    os.makedirs(os.path.join('itmo', 'pin', 'mobilki', 'k3140'), exist_ok=True)
    os.makedirs(os.path.join('world', 'russia', 'spb'), exist_ok=True)
    os.makedirs(os.path.join('math', 'linal'), exist_ok=True)


def make_files_set():
    """
    Function that creates base files.
    @return: None
    """
    open('student.txt', 'w').close()
    open('university.txt', 'w').close()
    open('people.txt', 'w').close()
    open('ege.txt', 'w').close()


def move_files_set():
    """
    Function that moves files to folders.
    @return: None
    """
    os.replace('student.txt', os.path.join('itmo', 'pin', 'mobilki', 'k3140', 'student.txt'))
    os.replace('university.txt', os.path.join('world', 'russia', 'spb', 'university.txt'))
    os.replace('people.txt', os.path.join('world', 'russia', 'people.txt'))
    os.replace('ege.txt', os.path.join('math', 'ege.txt'))


def walk_dirs():
    """
    Function that walks through directories.
    @return: None
    """
    for root, dirs, files in os.walk(os.getcwd()):
        print('Dir:', root)
        print('Files:\n' + '\n'.join(files))
        print()


def main():
    """
    Main function that runs all steps.
    @return: None
    """
    #1
    copy_file("task1.txt", "copy_task1.txt")
    #2
    move_file("copy_task1.txt", "task2.txt")
    make_dirs(os.path.join('labs', 'prog', 'lab3'))
    move_file('task2.txt', os.path.join('labs', 'prog', 'task2.txt'))
    #3
    make_empty_file("new_file.txt")
    move_file('new_file.txt', os.path.join('labs', 'prog', 'lab3', 'old_file.txt'))
    #4
    make_many_files(5)
    show_dir(os.getcwd())
    go_to(os.path.join('labs', 'prog', 'lab3'))
    show_dir_custom(os.path.join('labs', 'prog', 'lab3'))
    #5
    go_to(os.path.join('..', '..', '..'))
    make_and_del_dir("DEL")
    make_structure()
    make_files_set()
    move_files_set()

    walk_dirs()


if __name__ == "__main__":
    main()