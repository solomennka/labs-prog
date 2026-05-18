import os
from datetime import datetime
import stat


def make_file(name: str):
    """
    Function that creates file and writes directory content.
    @param name: str - file name
    @return: None
    """
    with open(name, 'w') as f:
        f.write('\n'.join(os.listdir()))


def check_exist(name: str):
    """
    Function that checks file existence.
    @param name: str - file name
    @return: None
    """
    if os.path.exists(os.path.join(os.getcwd(), name)):
        print("File exists")


def get_info(name: str) -> os.stat_result:
    """
    Function that prints file info and returns stat.
    @param name: str - file name
    @return: os.stat_result - file stat info
    """
    statinfo = os.stat(name)
    print("Size:", str(statinfo.st_size))
    print("Date of last modification:", datetime.fromtimestamp(statinfo.st_mtime))
    print("Date of last access:", datetime.fromtimestamp(statinfo.st_atime))
    print("Current user:", os.getlogin())
    return statinfo


def show_perm(statinfo: os.stat_result):
    """
    Function that prints file permissions.
    @param statinfo: os.stat_result - file stat info
    @return: None
    """
    print("Access level:", stat.filemode(statinfo.st_mode))


def set_perm_ro(name: str):
    """
    Function that sets read-only permissions.
    @param name: str - file name
    @return: None
    """
    os.chmod(os.path.join(os.getcwd(), name), 0o444)
    print('Access level change')


def set_perm_full(name: str):
    """
    Function that sets full permissions.
    @param name: str - file name
    @return: None
    """
    os.chmod(os.path.join(os.getcwd(), name), 0o666)
    print('Access level change')


def upd_stat(name: str) -> os.stat_result:
    """
    Function that updates stat info.
    @param name: str - file name
    @return: os.stat_result - file stat info
    """
    return os.stat(name)


def main():
    """
    Main function that runs all steps.
    @return: None
    """
    #1
    fname = 'task1.txt'
    make_file(fname)
    #2
    check_exist(fname)
    #3
    st = get_info(fname)
    #4
    show_perm(st)
    set_perm_ro(fname)
    st = upd_stat(fname)
    show_perm(st)
    set_perm_full(fname)
    st = upd_stat(fname)


if __name__ == "__main__":
    main()
