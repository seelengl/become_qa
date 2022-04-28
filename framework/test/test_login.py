from app.api.client import ApiClient
import pytest
import logging

logger = logging.get_logger()


@pytest.fixture
def api_session(scope='session'):
    ac = ApiClient()
    ac.login()
    yeild ac
    
def test_get_folders(api_session):
    assert api_session.get_folders() is not None
    
def test_get_file(api_session):
    assert api_session.get_file() is not None

def test_get_file_count():
    assert api_session.get_file_count() == 22
    
    
    ##assert ac.get_file_runs() is not None
    ##assert ac.get_file_analysis() is not None
    ##assert ac.get_files_artifacts() is not None
    
