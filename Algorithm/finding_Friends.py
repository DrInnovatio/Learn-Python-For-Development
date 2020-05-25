def print_all_friends(g, start):
    queue = []
    done = set()

    queue.append(start)
    done.add(start)

    while queue:
        p = queue.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                queue.append(x)
                done.add(x)

friends_info = {
    "Summer": ["John", "Justin", "Mike"],
    "John": ["Summer", "Justin"],
    "Justin": ["John", "Summer", "Mike", "May"],
    "Mike": ["Summer", "Justin"],
    "May": ["Justin", "Kim"],
    "Kim": ["May"],
    "Tom": ["Jerry"],
    "Jerry": ["Tom"]
}

print_all_friends(friends_info, "Mike")
print()
print_all_friends(friends_info, "Jerry")