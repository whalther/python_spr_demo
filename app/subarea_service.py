from re import sub
from connectionDB import Database
from flask import Flask, request, jsonify,redirect
from subarea_repository  import SubareaRepository
from model import subarea

class Subarea:
    _subareaRepository = ''
    def __init__(self):
        self._subareaRepository = SubareaRepository()

    def getSubAreas(self):
        
        cur = self._subareaRepository.getSubArea()
        
        dataArray = []
        for row in cur:#cursor
            mySubarea =subarea.SubArea()
            mySubarea.id = row[0]
            mySubarea.subarea_name = row[1]
            mySubarea.id_area = row[2]
            mySubarea.estado = row[3]            
            mySubarea.createdAt = row[4]
            mySubarea.updatedAt = row[5]
            dataArray.append(mySubarea.__dict__)
        
        return jsonify(dataArray)