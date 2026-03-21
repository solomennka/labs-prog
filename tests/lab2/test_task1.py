import asyncio
import pytest
from src.lab2.task1 import wait


@pytest.mark.asyncio
async def test_output1(capsys):
    """Test: check output"""
    await wait(1, "Two")
    output = capsys.readouterr()
    lines = output.out.strip().split('\n')
    assert lines == ["Two"]


@pytest.mark.asyncio
async def test_output2(capsys):
    """Test: check output"""
    await wait(1, "Hello program\n")
    output = capsys.readouterr()
    lines = output.out.strip().split('\n')
    assert lines == ["Hello program"]


@pytest.mark.asyncio
async def test_time1(capsys):
    """Test: check time"""
    start = asyncio.get_event_loop().time()
    await wait(3, "Hello program\n")
    end = asyncio.get_event_loop().time()
    assert end - start >= 3.0
    assert end - start < 3.5


@pytest.mark.asyncio
async def test_time2(capsys):
    """Test: check time"""
    start = asyncio.get_event_loop().time()
    await wait(0.1, "Hello program\n")
    output = capsys.readouterr()
    lines = output.out.strip().split('\n')
    assert lines == ["Hello program"]
    end = asyncio.get_event_loop().time()
    assert end - start >= 0.1
    assert end - start < 0.6
