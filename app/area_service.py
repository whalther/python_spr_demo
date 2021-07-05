import connectionDB 
from flask import Flask, request, jsonify,redirect
from area_repository import AreaRepository
from model import area

class Area:
    @staticmethod
    def getAreas():
    
        cur = AreaRepository().getArea()
        
        dataArray = []
        for row in cur:#cursor
            myArea =area.Area()
            myArea.id = row[0]
            myArea.areaName = row[1]
            myArea.estado = row[2]
            myArea.createdAt = row[3]
            myArea.updatedAt = row[4]
            dataArray.append(myArea.__dict__)
        
        return jsonify(dataArray)