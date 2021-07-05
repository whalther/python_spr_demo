from connectionDB import Database
from flask import Flask, request, jsonify

class SubareaRepository:

    _db=''
    def __init__(self):
        self._db = Database 

    def getSubArea(self):
        cur = self._db.getDB().cursor()
        cur.execute('''getSubAreas 1''')
        return cur