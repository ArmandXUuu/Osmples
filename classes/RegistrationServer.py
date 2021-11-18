# Le serveur "E"
# Il est l'autorité d'enregristrement des utilisateurs (le serveur qui CRÉER LES ACCÉS)

from typing import List
from classes.Server import Server
from classes.AdministrationServer import AdministrationServer as A
from utils.log_util import logger
from random import shuffle
from cryptoUtils.hashage import generate_uuid
from Crypto.Protocol.KDF import PBKDF2

class RegistrationServer(Server):

    def __init__(self):
        print("initiate a Serveur d'enregistrement")

    def generate_credentials(self, uuid_list: list):
        vote_codes = []

        for uuid in uuid_list:
            c_n = self.generate_secret_id(uuid)
            f = open("./data/credentials/" + uuid, "w")
            f.write(c_n)
            vote_codes.append(self.__generate_vote_code(c_n, uuid))
            f.close()
        return self.__shuffle_list(vote_codes)

    def generate_secret_id(self, uuid: str) -> str:
        c_n = generate_uuid(uuid)
        print("Secret id generated")
        return c_n

    @staticmethod
    def __generate_vote_code(c_n: str, uuid: str) -> bytes:  # Pub() function
        print("Code de vote pour c_n is generated")
       # logger.debug("TODO generate Pub(c_n) for {}".format(uuid))
        res = PBKDF2(c_n, bytes(uuid, "utf-8"))
        return PBKDF2(c_n, bytes(uuid, "utf-8"))

    def __shuffle_list(self, list_in: [str]) -> [str]:
        list_out = list_in
        shuffle(list_out)
        logger.debug("list shuffled and returned as is")
        return list_out
