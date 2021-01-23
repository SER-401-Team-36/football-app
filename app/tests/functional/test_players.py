import json
from flask_jwt_extended import create_access_token


def test_get_users(test_client, init_database):
    access_token = create_access_token('testuser')
    response = test_client.get('/players/', headers={
        'Authorization': 'Bearer {}'.format(access_token)
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
