from decimal import Decimal


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

print(gcd(7400249944258160101211, 247064529073450392704413))
print(int(7400249944258160101211 / 7400249944258160101211))