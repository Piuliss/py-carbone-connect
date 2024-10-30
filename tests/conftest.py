import pytest
from unittest.mock import Mock, MagicMock
import io

@pytest.fixture
def api_url():
  return "http://api.example.com"

@pytest.fixture
def mock_response():
  mock = Mock()
  mock.ok = True
  mock.content = b"mock content"
  mock.json.return_value = {"status": "success"}
  return mock

@pytest.fixture
def mock_error_response():
  mock = Mock()
  mock.ok = False
  mock.json.return_value = {"error": "Test error message"}
  return mock

@pytest.fixture
def sample_template_data():
  return {
      "name": "John Doe",
      "age": 30,
      "email": "john@example.com"
  }

@pytest.fixture
def sample_options():
  return {
      "convertTo": "pdf",
      "orientation": "portrait"
  }

@pytest.fixture
def mock_template_file():
  file = MagicMock()
  file.read.return_value = b"mock template content"
  file.name = "template.docx"
  return file