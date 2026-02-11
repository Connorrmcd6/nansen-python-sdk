import pytest
import respx

from nansen import AsyncNansen, Nansen


@pytest.fixture
def client():
    with Nansen(api_key="test-key") as c:
        yield c


@pytest.fixture
def async_client():
    return AsyncNansen(api_key="test-key")


@pytest.fixture
def mock_api():
    with respx.mock(base_url="https://api.nansen.ai/api/v1") as mock:
        yield mock
