from main import APP
import pytest


@pytest.fixture
def client():
    client = APP.test_client()

    yield client


def test_prediction(client):
    post_data = {
    }

    result = client.post('/prediction', json=post_data)

    assert result.status_code == 200
