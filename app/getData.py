import requests
import json
from . import app
from .models import db, tbl_zksession

def getDataApi(enddate, startdate, pageSize, pageNo, personPin):
    query_table = db.session.query(tbl_zksession).filter_by(id=1).first()
    cookie_string = query_table.cookie
    cookie = cookie_string.split(': ')

    url = app.config['URL_ENDPOINT']

    headers = {
        'Cookie' : cookie[1]
        }
    
    params = {
        'endDate': enddate, 
        'startDate': startdate,
        'pageNo' : pageNo,
        'pageSize' : pageSize,
        'personPin' : personPin
        }
    
    response = requests.request("GET", url, headers=headers, params=params)
    
    if response.status_code == 200:  # Check if the request was successful
        return response.json()
    else:
        # Handle error response if needed
        error_response = {
            "error": "Request failed with status code: {}".format(response.status_code)
        }
        return error_response
