def fast_mod(x: int, n: int, mod: int) -> int:
    """
    https://blog.csdn.net/weixin_46395886/article/details/113103043?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.showsourcetag&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.showsourcetag
    :param x:
    :param n:
    :param mod:
    :return:
    """
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

