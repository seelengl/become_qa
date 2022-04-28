from app.api.client import ApiClient

def test_login():
    ac = ApiClient()
    assert ac.login() is not None
    assert ac.get_folders() is not None
    assert ac.get_file() is not None
    assert ac.get_file_count() is not None
    assert ac.get_file_runs() is not None
    assert ac.get_file_analysis() is not None
    assert ac.get_files_artifacts() is not None