# Nur ein simples Beispiel um zu zeigen, wie über die API Daten abgefragt werden können; hier: die Anzahl der Module im Herbstsemester 21

import httplib2, requests
import json
from flask import request, send_file, render_template, make_response
from flask_api import FlaskAPI, status
from functools import wraps
import os
import json
import httplib2, requests
import sys
from math import sqrt

app = FlaskAPI(__name__)

queue = list()
"""
http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
url = 'http://localhost:5000/solver/'
headers = {'Content-type':'application/json','Accept':'application/json','Authorization':'Token token="abc"'}
resp, content = http.request(url, 'GET', headers=headers)
print(resp)
print(content)
"""

@app.route("/idms/semester/", methods=['GET'])
def get_semester():
    """
    Get all semester data of a particular semester
    """
    with open('../semesters.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


@app.route("/idms/occasions/", methods=['GET'])
def get_occasions():
    """
    Get all occasions of a particular semester
    """
    with open('../occasions_h21.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


@app.route("/idms/lecturers/", methods=['GET'])
def get_lecturers():
    """
    Get all lecturers of a particular semester
    """
    with open('../employees_h21.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


@app.route("/idms/classes/", methods=['GET'])
def get_classes():
    """
    Get all occasions of a particular semester
    """
    with open('../classes_h21.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


@app.route("/idms/rooms/", methods=['GET'])
def get_rooms():
    """
    Get all rooms of a particular semester
    """
    with open('../Rooms.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data

@app.route("/idms/penalties/", methods=['GET'])
def get_penalties():
    """
    Get all penalties of a particular semester
    """
    with open('../input_data/penalties.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


if __name__ == "__main__":
    app.run(debug=False, port=4711, host="localhost")

# Get the data of the first Anlass as a Python dictionary and print it out:
# print(data[0])
