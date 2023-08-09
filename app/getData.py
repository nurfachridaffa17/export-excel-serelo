import requests
import json
from . import app

def getDataApi(enddate, startdate, pageSize, pageNo, personPin):
    url = app.config['URL_ENDPOINT']
    headers = {
        'Cookie': app.config['HEADERS_ENDPOINT']
        }
    payload = {
        'endDate': enddate, 
        'startDate': startdate,
        'pageNo' : pageNo,
        'pageSize' : pageSize,
        'personPin' : personPin
        }
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    if response.status_code == 200:  # Check if the request was successful
        return response.json()
    else:
        # Handle error response if needed
        error_response = {
            "error": "Request failed with status code: {}".format(response.status_code)
        }
        return error_response
