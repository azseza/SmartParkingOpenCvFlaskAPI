from flask_restful import request, Resource
from flask_jwt_extended import jwt_required
import logging
import numpy as np
from database.models import Payment

class Money(Resource):
    """
    Rest Resource for having multiple statistics
    """
    def monthly(self):
        """
        Flask resource to calculate the ammount of monthly income 
        of all the parking(from Payment Document)
        """
        pipeline = [
            
        ]
        returnStatement = Payment.objects().aggregate(pipeline)
        return returnStatement, 200 

    def yearly(self):
        """
        Flask resource to calculate the yearly amount of yearly
        income accumulated by all the parkings (calculated from Payment)
        """
        pipeline = []
        returnStatement = Payment.objects().aggregate(pipeline)
        return returnStatement, 200

