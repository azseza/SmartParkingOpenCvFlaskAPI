"""Authentification handeleing"""
from database.models import Users
from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
import datetime
import cv2
import numpy as np

class SignupApi(Resource):
    """Sign up Resource """
    def post(self):
        """Create a user"""
        body = request.get_json()
        print(body)
        user = Users(**body)
        print("cachedd")
        user.hash_password()
        user.save()
        print("saved")
        id = user.id
        return {'id' : str(id) }, 200
    
    def put(self, id):
        """
        Image extension must be png
        """
        r = request
        try:
            nparr = np.fromstring(r.data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            user = Users.objects.get(id = id)
            user.image.put(img, content_type = 'image/png')  
            user.save()
            return "Done posting inmage ", 201
        except:
            return "Bad Image extension", 401 


class LoginApi(Resource):
    """Login Resource"""
    def post(self):
        """login as a user"""
        body = request.get_json()
        user = Users.objects.get(username=body.get('username'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            raise Exception
        expires = datetime.timedelta(hours=12)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200
