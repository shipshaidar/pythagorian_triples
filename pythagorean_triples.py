

def pythagorian_triple(m: int, n: int) -> tuple:
    if gcd(m, n) == 1 and m > n and (is_even(m) ^ is_even(n)):
        x: int = 2 * m * n
        y: int = m**2 - n**2
        z: int = m**2 + n**2
        return x, y, z
    else:
        return "NA"


def gcd(a: int, b: int) -> int:
    r: int = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)
    return 1


def is_even(n: int) -> bool:
    return n % 2 == 0


a = pythagorian_triple(2, 1)
print(a)