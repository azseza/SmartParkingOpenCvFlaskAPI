"""
Application initialization file 
This file is the entry point for running the Application
"""
from flask import Flask, jsonify
from flask_restful import Api
from resources import routes
from database.db import initialize_db
from flask_jwt_extended import JWTManager
import logging
import json
UPLOAD_FOLDER = '/upoad'
def logger():
    logger = logging.getLogger('Main Server')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


log = logger()

log.debug("initialisation De l'application ..")
app = Flask(__name__)

log.debug("initialisation de la Base de données")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['JWT_SECRET_KEY'] = "Il faut changer ça"

app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb://localhost/AgentParging'
}

log.debug("initialisation")

api = Api(app)

#bcrypt = Bcrypt(app)

jwt = JWTManager(app)

initialize_db(app)

routes.initialize_routes(api)
log.debug("Running !! ")
app.run(port=3070, debug=True)

