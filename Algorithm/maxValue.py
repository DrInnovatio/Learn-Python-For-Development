def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n):
        if a[i] > max_v:
            max_v = a[i]
    return max_v


def find_max_index(b):
    n = len(b)
    max_idx = 0
    for j in range(1, n):
        if b[j] > b[max_idx]:
            max_idx = j
    return max_idx


def min_value(c):
    n = len(c)
    min_v = c[0]
    for k in range(1, n):
        if c[k] < min_v:
            min_v = c[k]
    return min_v


v = [3, 1, 5, 11, 8]
print(find_max(v))
print(find_max_index(v))
print(min_value(v))
