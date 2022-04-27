import requests
from config.conf import Config
class BaseRequests:
    """Class for calling HTTP requests"""
    def form_url(self, url):
        """Method to concat basse url and api path"""
        return Config.BASE_URL + url
    def get(self, path, params):
        """Reimplementation of GET method"""
        url = self.form_url(path)
        return requests.get(url, params)

    def post(self, path, params):
        """Reimplementation of POST method"""
        url = self.form_url(path)
        return requests.post(url, params)