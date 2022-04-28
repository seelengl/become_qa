from app.api.urls import Urls
from app.api.base_requests import BaseRequests
from config.config import Config


class ApiClient(BaseRequests):
    def __init__(self) -> None:
        self.token = None

    def login(self):
        """Method to execute login"""
        r= self.post(Urls.LOGIN, json={"expiry": 86400, "login_form": "logim page"}, headers={'Authorization': Config.LOGIN_TOKEN})
        self.token = r.json().get('token')
        r.raise_for_status()
        return self.token

    def get_folders(self):
        """Method to get Files - root folder"""
        params = {
            'breadcrumbs': '0',
            'offset': '0',
            'limit': '1000',
            'folder_id': '84c966d5-8dce-429d-8f92-44d5e28b1581',
            '_': '1622700773180',
        }
        r = self.get(Urls.FOLDERS_ITEMS, params, headers={'x-token' : self.token})
        self.items_folder =r.json().get('items')
        r.raise_for_status()
        return self.items_folder

    def get_file(self):
        """Method to get Files - specific folder"""
        schema = {
            'breadcrumbs': '0',
            'offset': '0',
            'limit': '1000',
            'folder_id': '84c966d5-8dce-429d-8f92-44d5e28b1581',
            '_': '1622700773180',
        }
        r = self.get(Urls.FILES_ITEMS, schema, headers={'x-token' : self.token})
        self.items_files = r.json().get('items')
        r.raise_for_status()
        return self.items_files

    def get_file_count(self):
        """Method to get Files Count"""
        query_string = {'folder_id': '84c966d5-8dce-429d-8f92-44d5e28b1581'}
        r = self.get(Urls.FILES_COUNT, query_string, headers={'x-token' : self.token})
        self.count = r.json().get('total')
        r.raise_for_status()
        return self.count

    def get_file_runs(self):
        """Method to get File Results - Get Runs"""
        r = self.get(Urls.FILES_RUNS, headers={'x-token' : self.token})
        self.runs = r.json().get('runs')
        r.raise_for_status()
        return self.runs

    def get_file_analysis(self):
        """Method to get File Results - Get Analyses"""
        r = self.get(Urls.FILES_ANALYSIS, headers={'x-token' : self.token})
        self.analysis = r.json().get('analysis')
        r.raise_for_status()
        return self.analysis

    def get_files_artifacts(self):
        """Method to get File Results - Get Artifacts"""
        r = self.get(Urls.FILES_ARTIFACTS, headers={'x-token' : self.token})
        self.artifacts = r.json().get('artifacts')
        r.raise_for_status()
        return self.artifacts




