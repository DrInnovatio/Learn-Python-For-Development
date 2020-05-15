def sel_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j

        a[i], a[min_idx] = a[min_idx], a[i]


d = [3, 5, 1, 2, 6, 4, 7]

sel_sort(d)
print(d)


f = 1
g = 2
h = 3

f,g,h = h,f,g

print(f,g,h)