"""
Rest resource qui permet l'initilisation d'un parking
""" 
from flask_restful import Resource
from flask import Response, request
from flask_jwt_extended import jwt_required
from flask_jwt_extended import current_user
from database.models import Parkings, ParkingLot
from OpenCvScripts.MonitorProcess import MonitorThread
import threading


class InitilizeAParking(Resource):
    """
    Flask Resource qui permet l'initilisation & l'activation d'un parking
    """
    @jwt_required()
    def post(self):
        """
        Function that initializes a parking object 
        sent via json
        only a 'sUdO' User can do this
        """
        to_add = request.get_json(force=True)
        new_park = Parkings(**to_add)
        new_park.save()
        returnStatement = {"created_id":"new_park.ParkingID"}
        return returnStatement, 201

class ActivateParking(Resource):
        @jwt_required()
        def get(self):
            """
            Function that activates a monitor parkign process 
            {
                "parkId":"<parkId>",
                "vidFeedSource":"<url>"
            }
            """
            try:
                data = request.get_json()
                mon = MonitorThread(data.get("vidFeedSource"), data.get("parkId"))
                monitor_thread = threading.Thread(target=mon.start, args=[data.get("vidFeedSource"), data.get("parkId")])
                monitor_thread.start()
                return "Process Strated", 200
            except AssertionError:
              return "You are not allowed here ", 404

        @jwt_required()
        def getall(self):
            parkings = Parkings.objects().to_json()
            return Response(parkings, mimetype="application/json", status=200) 
