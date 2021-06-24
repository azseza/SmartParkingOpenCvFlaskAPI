"""
Script : Define modeles of the database
"""
from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from mongoengine import (EmbeddedDocument, EmbeddedDocumentListField, DateTimeField,
                         connect, DecimalField, StringField, EmbeddedDocumentField,
                         ListField, Document, PolygonField, ReferenceField,
                         URLField, BooleanField, PointField, FileField)

OCCUPATION = ('L', 'O')
ROLES = ['Public','sUdO','PriVate']





class ParkingLot(EmbeddedDocument):
    """
    Define a parking lot object
    """
    _id = DecimalField(required=True)
    ImageCoordonates = PolygonField(required=True)
    GpsCoordinates = PointField(required=True)
    LotStatus = StringField(max_length=1, required=True,
                                   choices=OCCUPATION)
    tarif = DecimalField(required=False, default=1.5)


class Parkings(Document):
    """
    Define the parking object
    could be defined in code or from yaml file
    """
    # Status de l'initiation du parking
    ParkingInitStatus = StringField(required=True)
    # Vis à vis GestionParkignApi et GestUtilisateurAPi
    ParkingID = DecimalField(primary_key=True, max_value=999,
                                required=True)
    # Nom Du parking
    ParkingName = StringField(max_length=50, required=True, unique=True)
    # Capacité du parking, scarped dupuis *.ini
    ParkingCapacity = DecimalField(max_value=100, required=False)
    # Coord {"ParkingGps":(Long,Lat)} du parking, scarped depuis *.ini
    ParkingLotCoordinates = EmbeddedDocumentListField(ParkingLot)
    # Adresse du parking
    ParkingAdress = StringField(max_length=50)
    # Pid du monotoring du parking
    ParkingPID = DecimalField(required=False, unique=True)
    # Adresse du parking pour le monitoring
    ParkingDirectLink = URLField(unique=True)


class Users(Document):
    """
    User table
    """
    id = DecimalField(primary_key=True, required=True)
    username = StringField(max_length=500, required=True)
    password = StringField(max_length=500, required=True)
    role = StringField(choices=ROLES, required=True)
    dateNaissance = DateTimeField(required=False)
    dateInscription = DateTimeField(required=False)
    image = FileField(required=False)
 
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Reservation(Document):
    """
    Reservation table
    """
    clientQuiReserve = ReferenceField(Users)
    parkingReservee = ReferenceField(Parkings)
    lotReservee = EmbeddedDocumentField(ParkingLot)
    dateReservation = DateTimeField(required=True)
    nobrHeuresReservee = DecimalField(min_value=1, required=True)


class Ticket(Document):
    """
    Table ticket
    """
    dateEntree = DateTimeField(required=True)
    dateSorite = DateTimeField(required=True)


class Payment(Document):
    """
    Table Payement
    """
    numTransaction = DecimalField(required=True)
    montantPayee = DecimalField(required=True)
    datepayement = DateTimeField(required=True)
    modePayement = StringField(required=True)
