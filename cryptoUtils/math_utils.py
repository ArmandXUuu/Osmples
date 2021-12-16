from utils.const import *


# Euclid part
# @Thang Long C.
def euclide(a: int, b: int) -> int:
    if b == 0:
        return a
    return euclide(b, a % b)


def euclide_etendu(a: int, b: int) -> tuple:
    if b == 0:
        return a, 1, 0
    else:
        (pgcd, u, v) = euclide_etendu(b, a % b)
        return pgcd, v, u - (a // b) * v


def pgcd(a: int, b: int) -> int:
    return euclide(a, b)


def pgcd_1(a, b):
    """
    Stein algorithm
    :param a: input 1
    :param b: input 2
    :return: the PGCD of a and b
    """
    if a == b:
        return a
    if (a & 1) == 0 and (b & 1) == 0:
        return pgcd_1(a >> 1, b >> 1) << 1
    elif (a & 1) == 0 and (b & 1) != 0:
        return pgcd_1(a >> 1, b)
    elif (a & 1) != 0 and (b & 1) == 0:
        return pgcd_1(a, b >> 1)
    else:
        big = max(a, b)
        small = min(a, b)
        return pgcd_1(big - small, small)


def inverse_exists(number: int, modulo: int) -> bool:
    return pgcd(number, modulo) == 1


def find_inverse_bezout(number: int, modulo: int) -> int:
    inverse = None
    if inverse_exists(number, modulo):
        (_, u, _) = euclide_etendu(number, modulo)
        inverse = u % modulo
    return inverse


def fast_mod(x: int, n: int, mod=p) -> int:
    """
    https://blog.csdn.net/weixin_46395886/article/details/113103043?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.showsourcetag&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.showsourcetag
    :param x:
    :param n:
    :param mod:
    :return:
    """
    x = int(x)
    n = int(n)
    result = 1
    b = x

    while True:
        temp = n
        if n % 2 == 1:
            result = result * b % mod

        b = b * b % mod
        n = n // 2

        if temp < 1:
            return result
