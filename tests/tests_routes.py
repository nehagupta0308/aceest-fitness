import json
from app import create_app

def test_home_status_code():
    app = create_app()
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200

def test_home_message():
    app = create_app()
    client = app.test_client()
    resp = client.get('/')
    data = resp.get_json()
    assert data["message"] == "ACEest Fitness API running"

def test_echo():
    app = create_app()
    client = app.test_client()
    payload = {"name": "Neha"}
    resp = client.post('/echo', json=payload)
    data = resp.get_json()
    assert data["you_sent"]["name"] == "Neha"
