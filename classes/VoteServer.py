# Le serveur "S" :
# Il est le serveur de vote, celui sur les électeur mettent leur bulletin

from classes.Server import Server
from utils.log_util import logger
from cryptoUtils.math_utils import find_inverse_bezout
from cryptoUtils.zero_knowledge import *


class VoteServer(Server):
    vote_codes = []
    vote = None

    def __init__(self):
        super().__init__("I am a VoteServer")
        logger.debug("A Vote Server was initiated")

    def set_vote(self, vote):
        self.vote = vote
        self.vote_codes = self.vote.vote_codes

    def execute_audit(self):
        for bulletin in self.vote.bulletins:
            if bulletin.voter_code_vote not in self.vote_codes:
                logger.debug("ALERT, vote_code non trouvé")
                continue

            chal, w = generate_chal(bulletin.signature[1][1], bulletin.voter_uuid)

            if zero_knowledge_verify(w, json_read(bulletin.voter_uuid, "c_n"), chal, bulletin.signature[1][1], bulletin.voter_uuid):
                logger.debug("Zero-Knowledge Proof passed !")
            else:
                logger.debug("Zero-Knowledge Proof NOT PASSED !")
            if zero_knowledge_verify(w, json_read(bulletin.voter_uuid, "c_n")+"d", chal, bulletin.signature[1][1], bulletin.voter_uuid):
                logger.debug("Zero-Knowledge Proof passed !")
            else:
                logger.debug("Zero-Knowledge Proof NOT PASSED !")

    def counting(self):
        # init
        candidates = self.vote.candidates
        candidates_count = {}
        candidate_num = len(candidates)
        for i in range(1, candidate_num+1):
            candidates_count[i] = 0

        # count
        for bulletin in self.vote.bulletins:
            candidates_count[decrypt_vote(11, *bulletin.vote_chiffre)] += 1

        for i in range(1, candidate_num + 1):
            print("there is " + str(candidates_count[i]) + " for " + candidates[i])


def encrypt_vote(alpha: int, message: int) -> tuple:
    r = randint(1, p)
    c_1 = fast_mod(g, r)
    h = fast_mod(alpha, r)
    c_2 = message * h % p
    return c_1, c_2, h


def decrypt_vote(alpha: int, c_1: int, c_2: int, h: int) -> int:
    h_inv = find_inverse_bezout(h, p)
    return c_2 * h_inv % p
