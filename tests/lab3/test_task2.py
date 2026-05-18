import os
import pytest

from src.lab3.task2 import (
    copy_file,
    move_file,
    make_dirs,
    make_empty_file,
    make_many_files,
    show_dir,
    show_dir_custom,
    go_to,
    make_and_del_dir,
    make_structure,
    make_files_set,
    move_files_set,
    walk_dirs)


@pytest.fixture(autouse=True)
def cleanup():
    """Fixture: clean environment"""
    files = [
        "a.txt", "b.txt", "task1.txt", "copy_task1.txt",
        "task2.txt", "new_file.txt",
        "student.txt", "university.txt", "people.txt", "ege.txt"
    ]
    for f in files:
        if os.path.exists(f):
            os.remove(f)
    dirs = ["labs", "itmo", "world", "math", "DEL"]
    for d in dirs:
        if os.path.exists(d):
            import shutil
            shutil.rmtree(d)

    yield

    for f in files:
        if os.path.exists(f):
            os.remove(f)

    for d in dirs:
        if os.path.exists(d):
            import shutil
            shutil.rmtree(d)


def test_copy_file():
    """Test: copy file"""
    with open("a.txt", "w") as f:
        f.write("hello")
    copy_file("a.txt", "b.txt")
    assert os.path.exists("b.txt")
    with open("b.txt") as f:
        assert f.read() == "hello"


def test_move_file():
    """Test: move file"""
    open("a.txt", "w").close()
    move_file("a.txt", "b.txt")

    assert not os.path.exists("a.txt")
    assert os.path.exists("b.txt")


def test_make_dirs():
    """Test: create dirs"""
    make_dirs(os.path.join("x", "y", "z"))
    assert os.path.exists(os.path.join("x", "y", "z"))


def test_make_empty_file():
    """Test: empty file"""
    make_empty_file("a.txt")
    assert os.path.exists("a.txt")
    assert os.path.getsize("a.txt") == 0


def test_make_many_files():
    """Test: many files"""
    make_many_files(3)
    for i in range(3):
        assert os.path.exists(f"file_{i}.txt")


def test_show_dir(capsys):
    """Test: output dir"""
    make_empty_file("a.txt")
    show_dir(os.getcwd())

    output = capsys.readouterr()
    assert "Contents of the script folder:" in output.out


def test_show_dir_custom(capsys):
    """Test: custom dir output"""
    make_empty_file("a.txt")
    show_dir_custom("test")

    output = capsys.readouterr()
    assert "Contents of the folder test:" in output.out


def test_go_to():
    """Test: change dir"""
    make_dirs("test_dir")
    go_to("test_dir")

    assert os.getcwd().endswith("test_dir")


def test_make_and_del_dir():
    """Test: create and delete dir"""
    make_and_del_dir("temp")
    assert not os.path.exists("temp")


def test_make_structure():
    """Test: structure created"""
    make_structure()
    assert os.path.exists(os.path.join("itmo", "pin", "mobilki", "k3140"))
    assert os.path.exists(os.path.join("world", "russia", "spb"))
    assert os.path.exists(os.path.join("math", "linal"))


def test_make_and_move_files():
    """Test: files moved"""
    make_structure()
    make_files_set()
    move_files_set()

    assert os.path.exists(os.path.join("itmo", "pin", "mobilki", "k3140", "student.txt"))
    assert os.path.exists(os.path.join("world", "russia", "spb", "university.txt"))
    assert os.path.exists(os.path.join("world", "russia", "people.txt"))
    assert os.path.exists(os.path.join("math", "ege.txt"))


def test_walk_dirs(capsys):
    """Test: walk output"""
    make_dirs("test_dir")
    walk_dirs()

    output = capsys.readouterr()
    assert "Dir:" in output.out
    assert "Files:" in output.out
    assert 'test_dir' in output.out