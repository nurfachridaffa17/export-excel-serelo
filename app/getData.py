import requests
import json
from . import app

def getData(enddate, startdate, pageSize, pageNo):
    url = app.config['URL_ENDPOINT']
    headers = {'Cookie': app.config['HEADERS_ENDPOINT']}
    payload = {
        'endDate': enddate, 
        'startDate': startdate,
        'pageNo' : pageNo,
        'pageSize' : pageSize
        }
    
    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()
