from functions.euclide import euclide, euclide_etendu
from functions.prime import euler_indicator, fermat, find_inverse_euler_fermat, inverse_exists, find_inverse_bezout, is_prime_number

def launch_euclide_tests():
    print("Launching euclide tests...")
    assert(euclide(11, 17) == 1)
    assert(euclide(17, 11) == 1)
    assert(euclide(12, 24) == 12)
    assert(euclide(9848945919, 516516517) == 1)
    assert(euclide_etendu(11, 17) == (1, -3, 2))
    assert(euclide_etendu(331, 771) == (1, -191, 82))

def launch_prime_tests():
    print("Launching prime tests...")
    assert(inverse_exists(11, 17) == True)
    assert(inverse_exists(4, 12) == False)
    assert(inverse_exists(17, 11) == True)
    assert(inverse_exists(12, 4) == False)
    assert(find_inverse_bezout(11, 17) == 14)
    assert(find_inverse_bezout(331, 771) == 580)
    assert(find_inverse_bezout(12, 4) == None)
    assert(is_prime_number(2) == True)
    assert(is_prime_number(3) == True)
    assert(is_prime_number(5) == True)
    assert(is_prime_number(7) == True)
    assert(is_prime_number(11) == True)
    assert(is_prime_number(13) == True)
    assert(is_prime_number(17) == True)
    assert(is_prime_number(4) == False)
    assert(is_prime_number(348) == False)
    assert(fermat(17) == 15)
    assert(fermat(771) == None)
    assert(euler_indicator(17) == 16)
    assert(euler_indicator(771) == 512)
    assert(find_inverse_euler_fermat(11, 17) == 14)
    assert(find_inverse_euler_fermat(331, 771) == 580)

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    print("Launching tests...")
    launch_euclide_tests()
    launch_prime_tests()
    elapsed = time.perf_counter() - start
    print(f"Tests ended. Took {elapsed:.05f} second(s).")
