import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'super secret key'
    URL_ENDPOINT = "http://192.168.88.79:8098/api/v2/transaction/list"
    HEADERS_ENDPOINT = "SESSION=MjlhMDc3YzktMTE1OS00Y2VhLTk0ZjYtZDRjOWI3YTdlNTU0"
