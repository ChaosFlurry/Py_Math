def gcd(a: int, b: int):
    a = abs(a)
    b = abs(b)

    if a == b:
        gcd = a
        return gcd
    else:
        while a != 0 and b != 0:
            t = b
            b = a % b
            a = t
        gcd = a + b
    return int(gcd)


def lcm(a, b):
    return a / gcd(a, b) * b
