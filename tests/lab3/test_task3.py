import os
import pytest

from src.lab3.task3 import (
    show_processes,
    process_info,
    kill_process,
    env_show,
    env_add,
    change_priority,
    system_info)


def test_show_processes(capsys):
    """Test: show processes output"""
    show_processes()
    output = capsys.readouterr()
    assert output.out != "" or output.err == ""


def test_process_info(capsys):
    """Test: process info output"""
    pid = os.getpid()
    process_info(pid)

    output = capsys.readouterr()
    assert output.out != "" or output.err == ""


def test_kill_process_invalid():
    """Test: kill process (invalid PID should not crash)"""
    # используем явно несуществующий PID
    try:
        kill_process(999999)
    except Exception:
        assert False


def test_env_show(capsys):
    """Test: environment variables output"""
    env_show()
    output = capsys.readouterr()
    assert "=" in output.out


def test_env_add():
    """Test: add environment variable"""
    env_add("TEST_VAR", "123")
    assert os.environ.get("TEST_VAR") == "123"


def test_change_priority_invalid():
    """Test: change priority (should not crash)"""
    try:
        change_priority(os.getpid(), 10)
    except Exception:
        assert False


def test_system_info(capsys):
    """Test: system info output"""
    system_info()
    output = capsys.readouterr()

    assert "System:" in output.out