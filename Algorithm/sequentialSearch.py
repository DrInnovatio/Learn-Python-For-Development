def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return i

    return "none"

v = [17, 92, 18, 33, 58, 7, 33, 42]

print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 7))
print(search_list(v, 1))
print(search_list(v, 42))
print(search_list(v, 900))
