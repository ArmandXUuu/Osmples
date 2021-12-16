from utils.const import p, g, q
from random import randint
from cryptoUtils.math_utils import fast_mod
from cryptoUtils.hashage import get_hashage_int
from utils.file_rw_utils import json_read


def generate_chal(s: int, uuid: str) -> tuple:
    """

    :param s: la signature
    :param uuid:
    :return:
    """
    w = randint(1, p)
    A = fast_mod(g, w)

    s_m_a = str(s) + uuid + str(A)

    return get_hashage_int(s_m_a), w


def zero_knowledge_verify(w: int, c_n, chal: int, s: int, uuid: str) -> bool:
    if type(c_n) is str:
        res = ""
        for char in c_n:
            res += str(ord(char))
        c_n = int(res)
    resp = (w - c_n * chal) % q

    v_k = json_read(uuid, "public_key")
    A = (fast_mod(g, resp) * fast_mod(v_k, chal)) % p
    s_m_a_prime = str(s) + uuid + str(A)
    h_prime = get_hashage_int(s_m_a_prime)

    return h_prime == chal
