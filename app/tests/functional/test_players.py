import json


def test_get_users(test_client, init_database):
    response = test_client.get('/players/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
