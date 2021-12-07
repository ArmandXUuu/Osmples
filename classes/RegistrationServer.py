# Le serveur "E"
# Il est l'autorité d'enregristrement des utilisateurs (le serveur qui CRÉER LES ACCÉS)
from classes.Server import Server
from utils.log_util import logger


class RegistrationServer(Server):
    def __init__(self):
        super().__init__("I am a RegistrationServer")
        logger.debug("A Registration Server was initiated")
