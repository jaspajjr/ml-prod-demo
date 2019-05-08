from main import APP
import pytest


@pytest.fixture
def client():
    client = APP.test_client()

    yield client


def test_prediction():
    post_data = {
    }

    result = client.post('/match', json=post_data)

    assert result.status_code == 200
