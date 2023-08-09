from flask import request, jsonify
from . import app
from . import getData
import os


@app.route('/api/v1/transaction', methods=['GET'])
def getTransaction():
    endDate = request.args.get('endDate')
    startDate = request.args.get('startDate')
    pageSize = request.args.get('pageSize')
    pageNo = request.args.get('pageNo')
    personPin = request.args.get('personPin')

    data = getData.getDataApi(endDate, startDate, pageSize, pageNo, personPin)

    return jsonify(data)