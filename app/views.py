from flask import request, jsonify
from . import app
from . import getData
import os
import pandas as pd
import openpyxl


@app.route('/api/v1/transaction', methods=['GET'])
def getTransaction():
    endDate = request.form.get('endDate')
    startDate = request.form.get('startDate')
    pageSize = request.form.get('pageSize')
    pageNo = request.form.get('pageNo')
    personPin = request.form.get('personPin')

    data = getData.getDataApi(endDate, startDate, pageSize, pageNo, personPin)

    try:
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    

@app.route('/api/v1/transaction/download', methods=['GET'])
def downloadTransaction():
    endDate = request.form.get('endDate')
    startDate = request.form.get('startDate')
    pageSize = request.form.get('pageSize')
    pageNo = request.form.get('pageNo')
    personPin = request.form.get('personPin')

    data = getData.getDataApi(endDate, startDate, pageSize, pageNo, personPin)

    



    