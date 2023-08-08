from flask import request, jsonify
from . import app
import cv2
from getData import getData


@app.route('/api/v1/transaction', methods=['GET'])
def getTransaction():
    endDate = request.form.get('endDate')
    startDate = request.form.get('startDate')
    pageSize = request.form.get('pageSize')
    pageNo = request.form.get('pageNo')

    data = getData(endDate, startDate, pageSize, pageNo)

    return data
