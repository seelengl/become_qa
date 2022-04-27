from app.api.apiclient import ApiClient

def test_dummy():
    assert ApiClient.login() is not None
