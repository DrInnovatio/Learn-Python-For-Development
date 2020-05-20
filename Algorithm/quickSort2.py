def quick_sort(a):
    n = len(a)

    if n <= 1:
        return a

    pivot = a[-1]
    group1 = []
    group2 = []

    for i in range(0, n - 1):
        if a[i] < pivot:
            group1.append(a[i])
        else:
            group2.append(a[i])

    return quick_sort(group1) + [pivot] + quick_sort(group2)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(d))
