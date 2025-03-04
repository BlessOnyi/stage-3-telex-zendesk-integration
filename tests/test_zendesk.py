import pytest
from services.zendesk import fetch_support_tickets, fetch_satisfaction_ratings, send_feedback_to_telex
from httpx import AsyncClient
from unittest.mock import AsyncMock, patch

# @pytest.mark.asyncio
# @patch("services.zendesk.httpx.AsyncClient.get")
# async def test_fetch_support_tickets(mock_get):
#     """Test fetching support tickets from Zendesk"""
#     mock_get.return_value = AsyncMock(status_code=200, json=AsyncMock(return_value={
#         "tickets": [{"id": 1, "subject": "Test Ticket", "status": "open"}]
#     }))

#     tickets = await fetch_support_tickets("https://example.zendesk.com", "test@example.com", "fake_token")
    
#     assert len(tickets) == 1
#     assert tickets[0]["subject"] == "Test Ticket"
@pytest.mark.asyncio
@patch("services.zendesk.httpx.AsyncClient.get")
async def test_fetch_support_tickets(mock_get):
    """Test fetching support tickets from Zendesk"""
    mock_get.return_value = AsyncMock(status_code=200)
    mock_get.return_value.json = AsyncMock(return_value={
        "tickets": [{"id": 1, "subject": "Test Ticket", "status": "open"}]
    })

    tickets = await fetch_support_tickets("https://example.zendesk.com", "test@example.com", "fake_token")
    
    assert len(tickets) == 1
    assert tickets[0]["subject"] == "Test Ticket"

@pytest.mark.asyncio
@patch("services.zendesk.httpx.AsyncClient.get")
async def test_fetch_satisfaction_ratings(mock_get):
    """Test fetching satisfaction ratings from Zendesk"""
    mock_get.return_value = AsyncMock(status_code=200, json=AsyncMock(return_value={
        "satisfaction_ratings": [{"id": 1, "score": "good", "comment": "Great support!"}]
    }))

    ratings = await fetch_satisfaction_ratings("https://example.zendesk.com", "test@example.com", "fake_token")
    
    assert len(ratings) == 1
    assert ratings[0]["score"] == "good"
    assert ratings[0]["comment"] == "Great support!"

@pytest.mark.asyncio
@patch("services.zendesk.httpx.AsyncClient.post")
async def test_send_feedback_to_telex(mock_post):
    """Test sending feedback data to Telex"""
    mock_post.return_value = AsyncMock(status_code=200)

    await send_feedback_to_telex("http://example.com", "https://example.zendesk.com", "test@example.com", "fake_token")

    mock_post.assert_called_once()