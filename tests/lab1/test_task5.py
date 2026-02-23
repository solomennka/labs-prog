import asyncio

import pytest

from src.lab1.task5 import func1, func2, main


@pytest.mark.asyncio
async def test_output_func1(capsys):
    """Test: check outputs func1"""
    await func1()
    output = capsys.readouterr()
    lines = output.out.strip().split('\n')
    assert lines == ["One", "Two", "Three"]


@pytest.mark.asyncio
async def test_output_func2(capsys):
    """Test: check outputs func2"""
    await func2()
    output = capsys.readouterr()
    lines = output.out.strip().split('\n')
    assert lines == ["Four", "Five", "Six", "Seven"]


@pytest.mark.asyncio
async def test_output_main(capsys):
    """Test: check outputs main"""
    await main()
    output = capsys.readouterr()
    lines = output.out.strip().split('\n')
    assert "One" in lines[0] or "One" in lines[1]
    assert "Four" in lines[0] or "Four" in lines[1]
    assert set(lines) == {"One", "Two", "Three", "Four", "Five", "Six", "Seven"}


@pytest.mark.asyncio
async def test_time_func1():
    """Test: check time func1"""
    start = asyncio.get_event_loop().time()
    await func1()
    end = asyncio.get_event_loop().time()
    assert end - start >= 5.0
    assert end - start < 5.5


@pytest.mark.asyncio
async def test_time_func2():
    """Test: check time func2"""
    start = asyncio.get_event_loop().time()
    await func2()
    end = asyncio.get_event_loop().time()
    assert end - start >= 5.0
    assert end - start < 5.5


@pytest.mark.asyncio
async def test_time_main():
    """Test: check time main"""
    start = asyncio.get_event_loop().time()
    await main()
    end = asyncio.get_event_loop().time()
    assert end - start >= 5.0
    assert end - start < 5.5


@pytest.mark.asyncio
async def test_time_main(capsys):
    """Test: multiple function launches"""
    for _ in range(3):
        await func1()
    output = capsys.readouterr()
    lines = output.out.strip().split('\n')
    assert len(lines) == 9
    assert lines.count("One") == 3
    assert lines.count("Two") == 3
    assert lines.count("Three") == 3





