# conftest.py - Pytest configuration and shared fixtures for hobbies project

import pytest
import os
import tempfile
from pathlib import Path
from typing import Generator, Any
from unittest.mock import Mock, patch

# Set testing environment
os.environ['TESTING'] = 'true'


# Basic fixtures
@pytest.fixture(scope="session")
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture(scope="function")
def mock_logger():
    """Mock logger for testing."""
    return Mock()


@pytest.fixture(scope="function")
def sample_data() -> dict[str, Any]:
    """Sample data for testing hobbies functionality."""
    return {
        "id": 1,
        "name": "Test Hobby",
        "description": "A test hobby for testing purposes",
        "category": "sports",
        "active": True,
        "metadata": {
            "created_at": "2025-01-01T00:00:00Z",
            "tags": ["test", "hobby", "sports"]
        }
    }


# File system fixtures
@pytest.fixture(scope="function")
def temp_file(temp_dir: Path) -> Generator[Path, None, None]:
    """Create a temporary file for testing."""
    test_file = temp_dir / "test_file.txt"
    test_file.write_text("Test hobby content")
    yield test_file


@pytest.fixture(scope="function")
def empty_temp_file(temp_dir: Path) -> Generator[Path, None, None]:
    """Create an empty temporary file for testing."""
    test_file = temp_dir / "empty_file.txt"
    test_file.touch()
    yield test_file


# Mock fixtures
@pytest.fixture(scope="function")
def mock_requests():
    """Mock requests library for HTTP testing."""
    with patch('requests.Session') as mock_session:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "success"}
        mock_response.text = '{"status": "success"}'
        mock_session.return_value.get.return_value = mock_response
        mock_session.return_value.post.return_value = mock_response
        yield mock_session


# Environment fixtures
@pytest.fixture(scope="function")
def test_env_vars():
    """Set test environment variables."""
    test_vars = {
        'TEST_MODE': 'true',
        'DEBUG': 'false',
        'DATABASE_URL': 'sqlite:///:memory:',
        'API_KEY': 'test-api-key',
        'HOBBIES_ENV': 'test'
    }

    # Store original values
    original_values = {}
    for key, value in test_vars.items():
        original_values[key] = os.environ.get(key)
        os.environ[key] = value

    yield test_vars

    # Restore original values
    for key, original_value in original_values.items():
        if original_value is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = original_value


# Project-specific fixtures
@pytest.fixture(scope="function")
def hobby_project_root():
    """Get the hobbies project root directory."""
    return Path(__file__).parent.parent


@pytest.fixture(scope="function")
def agent_os_path(hobby_project_root):
    """Get the .agent-os directory path."""
    return hobby_project_root / ".agent-os"


# Custom markers
def pytest_configure(config):
    """Configure pytest markers for hobbies project."""
    config.addinivalue_line("markers", "unit: mark test as a unit test")
    config.addinivalue_line("markers", "integration: mark test as an integration test")
    config.addinivalue_line("markers", "e2e: mark test as an end-to-end test")
    config.addinivalue_line("markers", "slow: mark test as slow running")
    config.addinivalue_line("markers", "agent_os: mark test as Agent OS related")
    config.addinivalue_line("markers", "hobby: mark test as hobby functionality")
    config.addinivalue_line("markers", "cli: mark test as CLI related")


# Pytest hooks
def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test location."""
    for item in items:
        # Add markers based on test file location
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        elif "e2e" in str(item.fspath):
            item.add_marker(pytest.mark.e2e)
            item.add_marker(pytest.mark.slow)

        # Add markers based on test file name
        if "agent_os" in str(item.fspath) or "agent" in str(item.fspath):
            item.add_marker(pytest.mark.agent_os)
        if "hobby" in str(item.fspath):
            item.add_marker(pytest.mark.hobby)
        if "cli" in str(item.fspath):
            item.add_marker(pytest.mark.cli)


# Time mocking fixture
@pytest.fixture(scope="function")
def mock_time():
    """Mock time functions for consistent testing."""
    import time
    import datetime

    fixed_time = datetime.datetime(2025, 1, 1, 12, 0, 0)
    fixed_timestamp = fixed_time.timestamp()

    with patch('time.time', return_value=fixed_timestamp), \
         patch('datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value = fixed_time
        mock_datetime.utcnow.return_value = fixed_time
        yield fixed_time


@pytest.fixture(scope="function")
def captured_logs(caplog):
    """Capture log messages for testing."""
    import logging
    caplog.set_level(logging.DEBUG)
    yield caplog