from cryptoUtils.helpers.functions.euclide import pgcd, euclide_etendu

def is_prime_number(number: int) -> bool:
    for n in range(2, number):
        if pgcd(n, number) > 1:
            return False
    return True

def inverse_exists(number: int, modulo: int) -> bool:
    return pgcd(number, modulo) == 1

def find_inverse_bezout(number: int, modulo: int) -> int:
    inverse = None
    if inverse_exists(number, modulo):
        (_, u, _) = euclide_etendu(number, modulo)
        inverse = u % modulo
    return inverse

def modular_power(number: int, power: int, modulo: int) -> int:
    result = 1
    while (power > 0):
        if (power % 2 == 1):
            result = (result * number) % modulo
        power = power // 2
        number = (number * number) % modulo
    return result

def fermat(modulo: int) -> int:
    power = None
    if is_prime_number(modulo):
        power = modulo - 2
    return power

def euler_indicator(modulo: int) -> int:
    result = 0
    if is_prime_number(modulo):
        result = modulo - 1
    else:
        for p in range(1, modulo):
            if pgcd(p, modulo) == 1:
                result += 1
    return result

def find_inverse_euler_fermat(number: int, modulo: int) -> int:
    inverse = None
    if inverse_exists(number, modulo):
        power = fermat(modulo)
        if power == None:
            power = euler_indicator(modulo) - 1
        else:
            power = power % modulo
        inverse = modular_power(number, power, modulo)
    return inverse