from flask import Flask, request, jsonify,redirect
from employees_repository import EmployeeRepository
from model import employee

class EmployeeService:
     
    _employeeRepository = ''

    def __init__(self):
        self._employeeRepository = EmployeeRepository()


    def getEmployees(self):
        
        data = self._employeeRepository.getEmployeesAll()
        
        dataArray = []
        for row in data:#cursor
            myemployee =employee.Employee()
            myemployee.id = row[0]            
            myemployee.type_document = row[1]
            myemployee.doc = row[2]
            myemployee.name = row[3]
            myemployee.last_name = row[4]   
            myemployee.id_subarea = row[5]  
            myemployee.subarea_name = row[8]                               
            myemployee.area_name = row[10]
            myemployee.id_area= row[11]
            dataArray.append(myemployee.__dict__)
        
        return jsonify(dataArray)
        
    def insert(self):
        return self._employeeRepository.insert()
    def update(self):
        return self._employeeRepository.update()        
