import pytest
from unittest.mock import patch, MagicMock
from src.collector import collect_show_tech


@patch("src.collector.ConnectHandler")
def test_collect_success(mock_connect):
    mock_conn = MagicMock()
    mock_conn.send_command.return_value = "TECH OUTPUT"
    mock_connect.return_value = mock_conn

    device = {
        "name": "R1",
        "host": "1.1.1.1",
        "username": "admin",
        "password": "pass",
        "device_type": "cisco_ios",
    }

    result = collect_show_tech(device)
    assert result is True


@patch("src.collector.ConnectHandler", side_effect=Exception("failure"))
def test_collect_failure(mock_connect):
    device = {
        "name": "R1",
        "host": "1.1.1.1",
        "username": "admin",
        "password": "pass",
        "device_type": "cisco_ios",
    }

    result = collect_show_tech(device)
    assert result is False

