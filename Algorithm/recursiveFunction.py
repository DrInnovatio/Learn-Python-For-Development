# factorial


def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


print(fact(1))
print(fact(0))
print(fact(8))
print(fact(9))
print(fact(10))

print("# =========================")


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(0))
print(factorial(2))
print(factorial(3))
print(factorial(7))
