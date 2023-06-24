from flask import request, send_file, render_template, make_response
from flask_api import FlaskAPI, status
from functools import wraps
import os
import json
import httplib2, requests
import sys
from math import sqrt

from Solver import run_solver

app = FlaskAPI(__name__)

queue = list()

@app.route("/", methods=['GET'])
def index():
     return {"title":"IDMS Example API"}


@app.route("/solver/", methods=['GET'])
#@require_api_token
def get_request():
    """
    Get a request from IDMS
    """

    http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
    headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Token token="abc"'}

    print("requests semester")
    url = 'http://localhost:4711/idms/semester/'
    resp, content = http.request(url, 'GET', headers=headers)
    semester = json.loads(content)
    print("get semester")

    print("requests occasions")
    url = 'http://localhost:4711/idms/occasions/'
    resp, content = http.request(url, 'GET', headers=headers)
    occasions = json.loads(content)
    print("get occasions")

    print("requests lecturers")
    url = 'http://localhost:4711/idms/lecturers/'
    resp, content = http.request(url, 'GET', headers=headers)
    lecturers = json.loads(content)
    print("get lecturers")

    print("requests classes")
    url = 'http://localhost:4711/idms/classes/'
    resp, content = http.request(url, 'GET', headers=headers)
    classes = json.loads(content)
    print("get classes")

    print("requests rooms")
    url = 'http://localhost:4711/idms/rooms/'
    resp, content = http.request(url, 'GET', headers=headers)
    rooms = json.loads(content)
    print("get rooms")

    print("requests penalties")
    url = 'http://localhost:4711/idms/penalties/'
    resp, content = http.request(url, 'GET', headers=headers)
    penalties = json.loads(content)
    print("get penalties")

    print("solver begins")
    run_solver(semester, occasions, lecturers, classes, rooms, penalties)
    return "solver has been finished"


if __name__ == "__main__":
    app.run(debug=False, port=35786, host="localhost")
