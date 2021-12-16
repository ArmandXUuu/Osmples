from cryptoUtils.hashage import get_hashage_int
from cryptoUtils.math_utils import find_inverse_bezout, fast_mod
from utils.const import p, g


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
    _, _, h = public_key
    s_1, s_2 = signature
    h_M_tilde = get_hashage_int(message_prime)
    left = (fast_mod(h, s_1, p) * fast_mod(s_1, s_2, p)) % p
    right = fast_mod(g, h_M_tilde, p)

    return left == right
