from database.models import Users
from flask_restful import Resource, request
from flask_jwt_extended import jwt_required


class GestionUstilisateurs(Resource):
    """
    Flask resource qui donne acces dea la gestion
    des utilisateurs
    """
    @jwt_required
    def get(self):
        """
        Get all public users
        """
        returnStatement = Users.objects.get(role='public')
        return {"data": returnStatement}, 200

    def get_by_id(self, idUser):
        """
        get all public users by id 
        """
        returnStatement = Users.objects.get(id=idUser)
        return {"data": returnStatement}, 200