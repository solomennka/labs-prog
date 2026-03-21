import asyncio
from unittest.mock import patch

import pytest

import src.lab2.task4 as task4
from src.lab2.task4 import print_message, no_stream, streams


@pytest.mark.asyncio
def test_output_time_no_stream(capsys):
    """Test: check output and time"""
    no_stream()
    output = capsys.readouterr()
    lines = output.out.strip().split('\n')
    assert lines == ["One", "Two", "Three"]
    t = no_stream()
    assert t >= 6.0
    assert t < 6.5


@pytest.mark.asyncio
async def test_output_print_message(capsys):
    """Test: check output"""
    await print_message("Hello program\n", 1)
    output = capsys.readouterr()
    lines = output.out.strip().split('\n')
    assert lines == ["Hello program"]


@pytest.mark.asyncio
async def test_time1_print_message(capsys):
    """Test: check time"""
    start = asyncio.get_event_loop().time()
    await print_message("Hello program\n", 1)
    end = asyncio.get_event_loop().time()
    assert end - start >= 1.0
    assert end - start < 1.5


@pytest.mark.asyncio
async def test_time2_print_message(capsys):
    """Test: check time"""
    start = asyncio.get_event_loop().time()
    await print_message("123)\n", 0.1)
    output = capsys.readouterr()
    lines = output.out.strip().split('\n')
    assert lines == ["123)"]
    end = asyncio.get_event_loop().time()
    assert end - start >= 0.1
    assert end - start < 0.6


def test_thread_count_streams():
    """Test: check call count"""
    with patch("threading.Thread") as MockThread:
        task4.streams()
        assert MockThread.call_count == 3


def test_thread_count_no_streams():
    """Test: check call count"""
    with patch("asyncio.run") as MockThread:
        task4.no_stream()
        assert MockThread.call_count == 3


def test_time_streams():
    """Test: check time"""
    t = streams()
    assert t >= 2.0
    assert t < 2.5
