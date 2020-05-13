def find_min_idx(a):
    n = len(a)
    min_idx = 0

    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    results = []
    while a:
        min_dix = find_min_idx(a)
        value = a.pop(min_dix)
        results.append(value)

    return results

d = [2,4,5,1,3]
print(sel_sort(d))
