# Le serveur "E"
# Il est l'autorité d'enregristrement des utilisateurs (le serveur qui CRÉER LES ACCÉS)

from classes.Server import Server
from classes.AdministrationServer import AdministrationServer as A
from utils.log_util import logger
from random import shuffle


class RegistrationServer(Server):

    def __init__(self):
        print("initiate a Serveur d'enregistrement")

    def generate_secret_id(self, a: A) -> [str]:
        uuids = a.get_uuids()
        vote_codes = []
        logger.debug(uuids)

        for uuid in uuids:
            # logger.debug(uuid)
            vote_codes.append(RegistrationServer.__generate_vote_code(uuid))

        print("Secret id generated")
        logger.debug("Vote_codes : {}".format(vote_codes))
        return vote_codes

    @staticmethod
    def __generate_vote_code(uuid: str) -> str:  # Pub() function
        print("Code de vote pour c_n is generated")
        logger.debug("TODO generate Pub(c_n) for {}".format(uuid))
        return "TODO {} + stuff = Pub(c_n)".format(uuid)

    def __shuffle_list(self, list_in: [str]) -> [str]:
        list_out = list_in
        shuffle(list_out)
        logger.debug("list shuffled and returned as is")
        return list_out
