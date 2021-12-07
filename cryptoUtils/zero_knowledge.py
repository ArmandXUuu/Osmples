from utils.const import *
from random import randint
from cryptoUtils.math_utils import fast_mod

def test():
    w = randint(0, p)
    A = fast_mod(g, w, p)
    resp = (w - c_n * chal) % q