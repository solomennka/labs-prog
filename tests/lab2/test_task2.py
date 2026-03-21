import asyncio
import pytest
from src.lab2.task2 import main


@pytest.mark.asyncio
async def test_output1(capsys):
    """Test: check output"""
    await main()
    output = capsys.readouterr()
    lines = output.out.strip().split('\n')
    assert lines == ["Two", "One", "Three"]


@pytest.mark.asyncio
async def test_time1(capsys):
    """Test: check time"""
    start = asyncio.get_event_loop().time()
    await main()
    end = asyncio.get_event_loop().time()
    assert end - start >= 3.0
    assert end - start < 3.5

