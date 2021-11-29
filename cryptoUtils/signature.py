from hashage import get_hashage_int
from math_utils import pgcd, fast_mod, pgcd_1, find_inverse_bezout
from utils.const import p, g
from random import randint


# El Gamal
def sign_signature(message: str) -> tuple:
    x = randint(2, p - 2)
    y = randint(2, p - 1)
    while pgcd_1(y, p - 1) != 1:
        y = randint(2, p - 1)
    y_inv = find_inverse_bezout(y, p - 1)
    h = fast_mod(g, x)
    h_M = get_hashage_int(message)

    s_1 = fast_mod(g, y)
    s_2 = (y_inv * (h_M - x * s_1)) % (p - 1)
    return (p, g, h), (s_1, s_2), x, y, y_inv, h_M


def verify_signature(public_key: tuple, signature: tuple, message_prime: str) -> bool:
    _, _, h = public_key  # Because p and q are "global const" TODO : Do we need to change p and q every time ?
    s_1, s_2 = signature
    h_M_tilde = get_hashage_int(message_prime)
    # left = (h ** s_1 * s_1 ** s_2) % p
    left = (fast_mod(h, s_1, p) * fast_mod(s_1, s_2, p)) % p
    right = fast_mod(g, h_M_tilde, p)

    return left == right  # TODO JE SUIS BLOQUÉ @Long


def verify_signature_1(public_key: tuple, signature: tuple) -> bool:
    p, g, h = public_key  # Because p and q are "global const" TODO : Do we need to change p and q every time ?
    s_1, s_2 = signature
    h_M_prime = 7
    #left = (h ** s_1 * s_1 ** s_2) % p
    left = (fast_mod(h, s_1, p) * fast_mod(s_1, s_2, p)) % p
    right = fast_mod(g, h_M_prime, p)

    return left == right