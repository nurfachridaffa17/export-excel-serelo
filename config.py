import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'super secret key'
    URL_ENDPOINT = "192.168.88.79:8098/api/v2/transaction/list"
    HEADERS_ENDPOINT = "SESSION=YTk1MjE3NDgtNGU3ZC00NDgxLTlmYmYtYWYzYzczMzY4MzA5"
