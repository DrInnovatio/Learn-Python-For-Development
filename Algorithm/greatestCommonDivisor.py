def gcd(a, b):
    i = min(a, b)   # To choose and store minimum value
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1


print(gcd(1, 5))
print(gcd(3, 6))
print(gcd(60, 24))
print(gcd(81, 27))


def Euclid(c, d):
    if d == 0:
        return c
    return Euclid(d, c % d)


print(Euclid(1, 5))
print(Euclid(3, 6))
print(Euclid(60, 24))
print(Euclid(81, 27))
