from flask import Flask, request, jsonify, make_response,redirect
import os

from werkzeug.wrappers import response
from employees_repository import EmployeeRepository 
import json
from employees_service import EmployeeService
from area_service import Area
from subarea_service import Subarea
from flask_cors import CORS

class App:
   
    app = Flask(__name__)
    CORS(app)


    @app.route('/ListEmployees', methods=['POST'])
    def getEmployees():
        #request.get_json()
        data = EmployeeService().getEmployees()        
        return (data)

    @app.route('/CreateEmployee',methods=['POST'])
    def insert():
        result = EmployeeService().insert()
        return jsonify({"status":200, "result": result})

    @app.route('/UpdateEmployee',methods=['POST'])
    def update():
        result = EmployeeService().update()
        return jsonify({"status":200, "result": result})


    @app.route('/ListArea',methods=['POST'])
    def getAreas():
        data = Area.getAreas()
        return(data)


    @app.route('/ListSubArea',methods=['POST'])
    def getSubAreas():
        data = Subarea().getSubAreas()
        return(data)


    if __name__ == '__main__':
        app.run( port=3000,debug=True)
