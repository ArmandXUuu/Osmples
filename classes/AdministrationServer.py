# Le serveur "A" :
# Il représente l'autorité d'administration de l'élection.

from classes.User import User, UserTypes
from classes.Server import Server
import time
from enum import Enum
from cryptoUtils.hashage import generate_uuid
from utils.log_util import logger
from utils.file_rw_utils import json_output
from utils.const import *

# from RegistrationServer import RegistrationServer as E
debug = True

class Bulletin:
    vote_id = 0
    voter_uuid = 0

    vote_chiffre = 0
    signature = 0

    def __init__(self, vote_id: int, voter_uuid: int, vote_chiffre = 0, signature = 0):
        self.vote_id = vote_id
        self.voter_uuid = voter_uuid
        self.vote_chiffre = vote_chiffre
        self.signature = signature


class Vote:
    id = 0

    __candidates = {}
    __starts_at = ""
    __ends_at = ""
    __choices_possible = 1

    alphas = dict()
    vote_codes = []

    bulletins = []  # liste de type Bulletin

    def __init__(self, candidates: dict, starts_at: str, ends_at: str, choices_possible: int = 1):
        self.__candidates = candidates
        self.__starts_at = starts_at
        self.__ends_at = ends_at
        self.__choices_possible = choices_possible

    def __str__(self):
        candidate_strings = []
        for k in self.__candidates.keys():
            candidate_strings.append("\t\t" + str(k) + " - " + self.__candidates[k])
        return "\033[1mInformations on this vote :\033[0m\n\t" \
               "You can only vote between {} and {}" \
               "\n\tCandidates are : \n\033[1;32m{}\033[0m\n\tYOU CAN JUST VOTE FOR \033[1;31m{}\033[0m PERSON(S) !\n" \
            .format(self.__starts_at, self.__ends_at,
                    '\n'.join(candidate_strings),
                    self.__choices_possible)

    def add_bulletin(self, bulletin: Bulletin):
        self.bulletins.append(bulletin)

    def get_alpha(self) -> int:
        alpha = 1
        for a in self.alphas.values():
            alpha *= a

        return alpha % p

    def get_candidates_num(self):
        return len(self.__candidates)


class AdministrationServer(Server):
    user_infos = dict()  # a dict contains uuid and user : {uuid: user}
    # votes = []
    vote = None

    def __init__(self):
        print("initiate a Administration server")

    def add_user(self, user: User):
        uuid = generate_uuid("user_Unique_ID for {}".format(user.__str__()))
        self.user_infos[uuid] = user  # for now we just deal with one vote a time. so no [[__user_list]] for now

        if user.user_type == UserTypes.TrustedDelegatedUser:
            self.vote.alphas[uuid] = user.public_key
        # else:
        #   self.vote.vote_codes.append(user.public_key)

        logger.debug(self.user_infos)
        json_output(self.user_infos, True)

    def get_uuids(self):
        uuids = []
        for uuid in self.user_infos.keys():
            if self.user_infos[uuid].user_type == UserTypes.Voter:
                uuids.append(uuid)
        return uuids

    def __str__(self):
        return "In administrater server A we have : {} - {}".format(self.user_infos, self.user_infos)

    def add_vote(self):
        if not debug:
            start_date = input("Date de début (YYYY-MM-DD) : ")
            end_date = input("Date de fin (YYYY-MM-DD) : ")
            candidates_input = input(
                "Saisir les candidats sous la forme 'nom prénom' et séparer chaque candidat par une virgule : ")
            liste_candidates = {}
            i = 1
            for candidat in candidates_input.split(','):
                liste_candidates[i] = candidat.strip()
                i += 1
            self.vote = Vote(liste_candidates, start_date, end_date)
        else:
            self.vote = Vote({1: "Macron", 2: "Obama", 3: "XI Jinping"}, "2021-11-11 00:00:00", "2022-01-01 12:59:59", 1)
