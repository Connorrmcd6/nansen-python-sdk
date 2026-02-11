import pytest

from nansen import AsyncNansen, Nansen


class TestClientInit:
    def test_api_key_from_param(self):
        client = Nansen(api_key="test-key")
        assert client.api_key == "test-key"
        client.close()

    def test_api_key_from_env(self, monkeypatch):
        monkeypatch.setenv("NANSEN_API_KEY", "env-key")
        client = Nansen()
        assert client.api_key == "env-key"
        client.close()

    def test_missing_api_key_raises(self, monkeypatch):
        monkeypatch.delenv("NANSEN_API_KEY", raising=False)
        with pytest.raises(ValueError, match="API key must be provided"):
            Nansen()

    def test_param_overrides_env(self, monkeypatch):
        monkeypatch.setenv("NANSEN_API_KEY", "env-key")
        client = Nansen(api_key="param-key")
        assert client.api_key == "param-key"
        client.close()

    def test_context_manager(self):
        with Nansen(api_key="test-key") as client:
            assert client.api_key == "test-key"

    def test_custom_base_url(self):
        client = Nansen(api_key="test-key", base_url="https://custom.api.com")
        assert client.base_url == "https://custom.api.com"
        client.close()

    def test_custom_timeout(self):
        client = Nansen(api_key="test-key", timeout=30.0)
        assert client.timeout == 30.0
        client.close()

    def test_custom_max_retries(self):
        client = Nansen(api_key="test-key", max_retries=5)
        assert client.max_retries == 5
        client.close()


class TestAsyncClientInit:
    def test_api_key_from_param(self):
        client = AsyncNansen(api_key="test-key")
        assert client.api_key == "test-key"

    def test_missing_api_key_raises(self, monkeypatch):
        monkeypatch.delenv("NANSEN_API_KEY", raising=False)
        with pytest.raises(ValueError, match="API key must be provided"):
            AsyncNansen()


class TestHeaders:
    def test_build_headers(self):
        client = Nansen(api_key="my-api-key")
        headers = client._build_headers()
        assert headers["apikey"] == "my-api-key"
        assert headers["content-type"] == "application/json"
        assert "nansen-python/" in headers["user-agent"]
        client.close()


class TestResourceAccess:
    def test_smart_money(self, client):
        assert client.smart_money is not None

    def test_profiler(self, client):
        assert client.profiler is not None

    def test_profiler_address(self, client):
        assert client.profiler.address is not None

    def test_tgm(self, client):
        assert client.tgm is not None

    def test_portfolio(self, client):
        assert client.portfolio is not None

    def test_points(self, client):
        assert client.points is not None

    def test_cached_property(self, client):
        assert client.smart_money is client.smart_money
