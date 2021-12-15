from cryptoUtils.math_utils import fast_mod, find_inverse_bezout
from utils.const import p, g
from random import randint


def eg_encrypt(h: int, message: str) -> tuple:
    c_2 = []
    y = randint(1, p-1)
    c_1 = fast_mod(g, y)
    s = fast_mod(h, y)

    for letter in message:
        c_2.append(ord(letter) * s % p)

    return c_1, c_2


def eg_decrypt(x: int, c_1: int, c_2: list) -> str:
    clear = ""
    s = fast_mod(c_1, x)
    s_inv = find_inverse_bezout(s, p)

    for letter_code in c_2:
        clear += chr(letter_code * s_inv % p)

    return clear
