import os

class Config:
    """Class defines all the configuration test framework"""
    BASE_URL='https://app.cosmosid.com'
    LOGIN_TOKEN= os.environ.get('LOGIN_TOKEN', None)