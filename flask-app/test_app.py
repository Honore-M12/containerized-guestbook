import pytest
from unittest.mock import patch, MagicMock
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    with patch('app.get_db') as mock_db:
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []
        mock_db.return_value.cursor.return_value = mock_cursor
        response = client.get('/')
        assert response.status_code == 200

def test_add_message(client):
    with patch('app.get_db') as mock_db:
        mock_db.return_value = MagicMock()
        response = client.post('/add', data={'message': 'test'})
        assert response.status_code == 302
