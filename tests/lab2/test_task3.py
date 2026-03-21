import asyncio
from unittest.mock import patch, AsyncMock
from unittest.mock import Mock
import pytest
import src.lab2.task3 as task3


def test_get_url():
    """Test: check status and time"""
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        status, t = task3.get_url("https://test.com")
        assert status == 200
        assert t >= 0


def test_no_async_output_and_time(capsys):
    """Test: check output and time"""
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        t = task3.no_async()
        output = capsys.readouterr()
        lines = output.out.strip().split("\n")
        assert len(lines) == 4
        assert all("200" in line for line in lines)
        assert t >= 0


def test_requests_count():
    """Test: check requests count"""
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        task3.no_async()
        assert mock_get.call_count == 4


@pytest.mark.asyncio
async def test_fetch():
    """Test: async fetch"""
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.text = AsyncMock()
    mock_context = AsyncMock()
    mock_context.__aenter__.return_value = mock_response
    mock_session = Mock()
    mock_session.get.return_value = mock_context
    await task3.fetch(mock_session, "https://test.com")
    assert mock_response.text.called


@pytest.mark.asyncio
async def test_with_async_task_count():
    """Test: check number of async tasks"""
    with patch("aiohttp.ClientSession") as MockSession, \
         patch("src.lab2.task3.fetch", new_callable=AsyncMock) as mock_fetch:
        mock_session = Mock()
        MockSession.return_value.__aenter__.return_value = mock_session
        await task3.with_async()
        assert mock_fetch.call_count == 4


@pytest.mark.asyncio
async def test_with_async_time():
    """Test: check execution time"""
    with patch("aiohttp.ClientSession") as MockSession:
        mock_session = Mock()
        MockSession.return_value.__aenter__.return_value = mock_session
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_context = AsyncMock()
        mock_context.__aenter__.return_value = mock_response
        mock_session.get.return_value = mock_context
        t = await task3.with_async()
        assert t >= 0