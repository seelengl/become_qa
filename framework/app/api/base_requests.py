import requests
from config.config import Config

class BaseRequests:
    """Class for colling HTTP requests"""
    def form_url(self, url):
        """method to concat base url and api path"""
        return Config.BASE_URL + url
    def get(self, path, *args, **kwargs):
        """Reimplementation of GET method"""
        url = self.form_url(path)
        return requests.get(url, *args, **kwargs)
    def post(self, path, *args, **kwargs):
        """Reimplementation of POST method"""
        url = self.form_url(path)
        return requests.post(url, *args, **kwargs)