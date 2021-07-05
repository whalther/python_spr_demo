from connectionDB import Database
from flask import Flask, json, request, jsonify
 
class EmployeeRepository:

    _db=''
    def __init__(self):
        self._db = Database 

    def getEmployeesAll(self):
        cur = self._db.getDB().cursor()
        cur.execute('''getAllEmployees''')  
        return cur


    def getEmployeesPagination(self,skip, limit):
        cur = self._db.getDB().cursor()
        cur.execute('''EmployeesPagination ?,?''',skip,limit)  
        return cur

    def insert(self):       
        cur = self._db.getDB().cursor()
        ok = False
        try:
            cur.execute('''createEmployee ?''', json.dumps(request.get_json()))
            cur.commit() 
            ok = True
        except:
            ok = False      
        return ok
    def update(self):       
        cur = self._db.getDB().cursor()
        ok = False
        try:
            cur.execute('''updateEmployee ?''', json.dumps(request.get_json()))
            cur.commit() 
            ok = True
        except:
            ok = False      
        return ok        


   
    