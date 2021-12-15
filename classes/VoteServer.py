# Le serveur "S" :
# Il est le serveur de vote, celui sur les électeur mettent leur bulletin

from classes.Server import Server
from utils.log_util import logger
from classes.AdministrationServer import Vote
from random import randint
from utils.const import p, g
from cryptoUtils.math_utils import fast_mod, find_inverse_bezout

class VoteServer(Server):
    vote_codes = []
    vote = None

    def __init__(self):
        super().__init__("I am a VoteServer")
        logger.debug("A Vote Server was initiated")

    def set_vote(self, vote):
        self.vote = vote
        self.vote_codes = self.vote.vote_codes


def encrypt_vote(alpha: int, message: int) -> tuple:
    r = randint(1, p)
    c_1 = fast_mod(g, r)
    h = fast_mod(alpha, r)
    c_2 = message * h % p
    return c_1, c_2, h


def decrypt_vote(alpha: int, c_1: int, c_2: int, h: int) -> int:
    h_inv = find_inverse_bezout(h, p)
    return c_2 * h_inv % p
