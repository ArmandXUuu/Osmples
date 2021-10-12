def euclide(a: int, b: int) -> int:
    if b == 0:
        return a
    return euclide(b, a % b)

def euclide_etendu(a: int, b: int) -> tuple:
    if b == 0:
        return (a, 1, 0)
    else:
        (pgcd, u, v) = euclide_etendu(b, a % b)
        return (pgcd, v, u - (a // b) * v)

def pgcd(a: int, b: int) -> int:
    return euclide(a,b)