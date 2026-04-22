import os
import stat
import pytest

from src.lab3.task1 import (
    make_file,
    check_exist,
    get_info,
    show_perm,
    set_perm_ro,
    set_perm_full,
    upd_stat)

file = "task1.txt"


@pytest.fixture(autouse=True)
def cleanup():
    """Fixture: create clean environment before and after test"""
    if os.path.exists(file):
        os.remove(file)
    yield
    if os.path.exists(file):
        os.remove(file)


def test_make_file():
    """Test: file is created"""
    make_file(file)
    assert os.path.exists(file)


def test_check_exist(capsys):
    """Test: check output of existence"""
    make_file(file)
    check_exist(file)
    output = capsys.readouterr()
    assert output.out.strip() == "File exists"


def test_get_info(capsys):
    """Test: check file info output"""
    make_file(file)
    get_info(file)
    output = capsys.readouterr()
    lines = output.out.strip().split('\n')
    assert "Size:" in lines[0]
    assert "Date of last modification:" in lines[1]
    assert "Date of last access:" in lines[2]
    assert "Current user:" in lines[3]


def test_permissions_output(capsys):
    """Test: check permissions output"""
    make_file(file)
    st = upd_stat(file)
    show_perm(st)
    set_perm_ro(file)
    st = upd_stat(file)
    show_perm(st)
    set_perm_full(file)
    st = upd_stat(file)
    show_perm(st)
    output = capsys.readouterr()
    lines = output.out.strip().split('\n')
    assert "Access level" in lines[0]
    assert "Access level change" in lines[1]
    assert "Access level" in lines[2]
    assert "Access level change" in lines[3]
    assert "Access level:" in lines[4]


def test_permissions_change():
    """Test: check real permission change"""
    make_file(file)
    set_perm_ro(file)
    st = upd_stat(file)
    perms = stat.filemode(st.st_mode)
    assert perms.startswith("-r--")
    set_perm_full(file)
    st = upd_stat(file)
    perms = stat.filemode(st.st_mode)
    assert perms.startswith("-rw-")


def test_upd_stat():
    """Test: check stat return type"""
    make_file(file)
    st = upd_stat(file)
    assert isinstance(st, os.stat_result)