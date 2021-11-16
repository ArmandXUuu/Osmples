# Le serveur "A" :
# Il représente l'autorité d'administration de l'élection.

from classes import User
from classes.Server import Server
import time
from enum import Enum
from cryptoUtils.hashage import generate_uuid
from utils.log_util import logger
from utils.file_rw_utils import json_output


# from RegistrationServer import RegistrationServer as E


class Vote:
    __candidates = []
    __starts_at = ""
    __ends_at = ""
    __choices_possible = 1

    def __init__(self, candidates: [str], starts_at: str, ends_at: str, choices_possible: int = 1):
        self.__candidates = candidates
        self.__starts_at = starts_at
        self.__ends_at = ends_at
        self.__choices_possible = choices_possible

    def __str__(self):
        return "########## Welcome ! ##########\n\033[1mInformations on this vote :\033[0m\n\t" \
               "You can only vote between {} and {}" \
               "\n\tCandidates are : \033[1;32m{}\033[0m\n\tYOU CAN JUST VOTE FOR \033[1;31m{}\033[0m PERSON(S) !" \
            .format(self.__starts_at, self.__ends_at,
                    ','.join(self.__candidates),
                    self.__choices_possible)


class AdministrationServer(Server):
    user_infos = dict()  # a dict contains uuid and user : {uuid: user}

    def __init__(self):
        print("initiate a Administration server")

    def add_user(self, user: User):
        uuid = generate_uuid("user_Unique_ID for {}".format(user.__str__()))
        self.user_infos[uuid] = user  # for now we just deal with one vote a time. so no [[__user_list]] for now
        logger.debug(self.user_infos)
        json_output(self.user_infos, True)

    def get_uuids(self):
        return list(self.user_infos.keys())

    def __str__(self):
        return "In administrater server A we have : {} - {}".format(self.user_infos, self.user_infos)


"""
    def get_vote_codes(self, e: E):
        vote_codes = e.generate_secret_id(self)
        logger.debug("IN A, we have vote_codes = {}".format(vote_codes))
"""
