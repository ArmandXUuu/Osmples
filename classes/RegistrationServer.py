# Le serveur "E"
# Il est l'autorité d'enregristrement des utilisateurs (le serveur qui CRÉER LES ACCÉS)
from random import choice, shuffle

from Crypto.Protocol.KDF import PBKDF2

from classes.Server import Server
from cryptoUtils.math_utils import fast_mod
from utils.const import ascii_vals_rev, ascii_vals, g, p
from utils.file_rw_utils import json_output
from utils.log_util import logger


class RegistrationServer(Server):
    def __init__(self):
        super().__init__("I am a RegistrationServer")
        logger.debug("A Registration Server was initiated")

    def generate_credentials(self, uuids: list):
        vote_codes = []

        for uuid in uuids:
            c_n, c_n_int = generate_secret_id()
            credentials = {"uuid": uuid, "c_n": c_n, "c_n_int": c_n_int, "code_vote": generate_vote_code(c_n, uuid),
                           "public_key": fast_mod(g, c_n_int)}
            json_output(credentials, "./data/credentials/" + uuid)
            vote_codes.append(credentials["code_vote"])

        return shuffle_list(vote_codes)


def generate_secret_id() -> tuple:
    """
    To generate the secret id -- c_n
    :return: c_n_str, a string, c_n_int, the int version
    """
    c_n = []
    c_ns_14 = ""
    for i in range(14):
        bit = choice(list(ascii_vals_rev.keys()))
        c_n.append(chr(bit))
        c_ns_14 += str(ascii_vals_rev[bit])
    c_n_15 = 53 - int(c_ns_14) % 53
    c_n_str = ''.join(c_n) + str(ascii_vals[c_n_15])

    # To generate an int
    res = ""
    for char in c_n_str:
        res += str(ord(char))
    c_n_int = int(res)
    return c_n_str, c_n_int


def generate_secret_s(c_n: str, uuid: str) -> bytes:
    return PBKDF2(c_n, bytes(uuid, "utf-8"))


def generate_vote_code(c_n: str, uuid: str) -> int:  # Pub() function
    print("Code de vote pour c_n is generated")
    return fast_mod(g, int.from_bytes(generate_secret_s(c_n, uuid), byteorder="little"), p)


def shuffle_list(list_in: [str]) -> [str]:
    list_out = list_in
    shuffle(list_out)
    logger.debug("list shuffled and returned as is")
    return list_out
