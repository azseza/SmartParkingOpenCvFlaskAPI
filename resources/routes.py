from . import parkingInit, stats, auth, transactions, useresResources


def initialize_routes(app):
    """
    Fonction qui initialise les routes de l'application
    """
    # Authentification 
    app.add_resource(auth.LoginApi, '/auth/login')
    app.add_resource(auth.SignupApi, '/auth/SignupApi')
    # Intialisation et activation d'un parking
    app.add_resource(parkingInit.InitilizeAParking, '/administrate/add')
    app.add_resource(parkingInit.ActivateParking, '/administrate/activate')
    app.add_resource(parkingInit.InitilizeAParking, '/administrate/getall', endpoint='getall')
    # Gestion de Clients
    app.add_resource(useresResources.GestionUstilisateurs, '/administrate/usesrs/get')
    app.add_resource(useresResources.GestionUstilisateurs, '/administrate/usesrs/getById/<int:idUser>', endpoint='get_by_id')
    # statistiques financéres
    app.add_resource(stats.Money, '/administrate/finance/monthly', endpoint='monthly')
    app.add_resource(stats.Money, '/administrate/finance/yearly', endpoint='yearly')
