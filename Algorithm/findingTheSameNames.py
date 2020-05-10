# Finding the names repeated


def find_same_name(a):
    n = len(a)
    result = set()  # making is an empty array.

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                result.add(a[i])

    return result


name = ["Tom", "Jerry", "Jerry", "Mike", "Tom",
        "Jane", "Matt", "Billy", "Will", "Jane"]

print(find_same_name(name))
