# Sum from 1 to N


def sum_n(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


print(sum_n(10))
print(sum_n(100))

# =========================


def anotherSum(k):
    return k * (k * 1) // 2


print(anotherSum(10))
print(anotherSum(1000))
