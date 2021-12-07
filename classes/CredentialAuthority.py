from random import shuffle, choice

from Crypto.Protocol.KDF import PBKDF2

from cryptoUtils.hashage import get_hashage_int, generate_uuid
from cryptoUtils.math_utils import find_inverse_bezout, fast_mod
from utils.const import p, g, ascii_vals, ascii_vals_rev
from utils.log_util import logger
from utils.file_rw_utils import json_output


# Signature El Gamal
def sign_signature(message: str, x: int, y: int) -> tuple:
    """
    This function helps to generate a signature by using El Gamal
    :param message: a message, string
    :param x: the private key chosen by the server `randint(2, p-2)`
    :param y: chosen by the server `randint(2, p-1)`
    :return: a tuple, the first element is a tuple (p,g,h), which is the public key ;
            the second element is another tuple (s_1, s_2) which is the signature itself.
    """
    y_inv = find_inverse_bezout(y, p - 1)
    h = fast_mod(g, x)
    h_M = get_hashage_int(message)

    s_1 = fast_mod(g, y)
    s_2 = (y_inv * (h_M - x * s_1)) % (p - 1)
    return (p, g, h), (s_1, s_2)


def verify_certificate(public_key: tuple, signature: tuple, message_prime: str) -> bool:
    """
    Aims to verify a certificate is validated or not (El Gamal)
    Usage : `verify_certificate(*cert_received)`
    Attention : a tuple is set to be unmodifiable, we can bypass that by transform tuples to lists @see classUnitTest.py
                @line 77
    :param public_key: a tuple (p,g,h)
    :param signature: a tuple (s_1, s_2)
    :param message_prime: the message received (message_tilde)
    :return: a bool, True if the validation passed, not vice versa
    """
    _, _, h = public_key  # Because p and q are "global const" TODO : Do we need to change p and q every time ?
    s_1, s_2 = signature
    h_M_tilde = get_hashage_int(message_prime)
    left = (fast_mod(h, s_1, p) * fast_mod(s_1, s_2, p)) % p
    right = fast_mod(g, h_M_tilde, p)

    return left == right


def generate_secret_id() -> str:
    """
    To generate the secret id -- c_n
    :return: c_n, a string
    """
    c_n = []
    c_ns_14 = ""
    for i in range(14):
        bit = choice(list(ascii_vals_rev.keys()))
        c_n.append(chr(bit))
        c_ns_14 += str(ascii_vals_rev[bit])
    c_n_15 = 53 - int(c_ns_14) % 53
    return ''.join(c_n) + str(ascii_vals[c_n_15])


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


def generate_credentials(uuids: list):
    vote_codes = []

    for uuid in uuids:
        c_n = generate_secret_id()
        credentials = {"c_n": c_n, "public_key": generate_vote_code(c_n, uuid)}
        json_output(credentials, "./data/credentials/" + uuid)
        vote_codes.append(credentials["public_key"])

    return shuffle_list(vote_codes)
