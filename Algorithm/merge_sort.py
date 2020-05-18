def merge_sort(a):
    n = len(a)

    if n <= 1:
        return a

    mid = n // 2
    group1 = merge_sort(a[:mid])
    group2 = merge_sort(a[mid:])

    result = []

    while group1 and group2:

        if group1[0] < group2[0]:
            result.append(group1.pop(0))
        else:
            result.append(group2.pop(0))

    while group1:
        result.append(group1.pop(0))
    while group2:
        result.append(group2.pop(0))
    return result


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

print(merge_sort(d))
