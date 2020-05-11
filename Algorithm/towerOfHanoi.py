# Recursive Python function to solve tower of hanoi


def TowerOfHanoi(n, source, destination, auxilliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)

        return
    TowerOfHanoi(n-1, source, auxilliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n-1, auxilliary, destination, source)


# Driver code
n = 4
TowerOfHanoi(n, 'A', 'B', 'C')

# A, C, B are the name of rods


print("============= Another code ================")
print("============= Another code ================")


# n : the number of disk
# from_pos : left pole
# to_pos : middle pole
# aux_pos : right pole

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, "->", to_pos)
        return

    hanoi(n - 1, from_pos, aux_pos, to_pos)

    print(from_pos, "->", to_pos)

    hanoi(n - 1, aux_pos, to_pos, from_pos)


print("n = 1")
hanoi(1, 1, 3, 2)

print("n = 2")
hanoi(2, 1, 3, 2)

print("m = 3")
hanoi(3, 1, 3, 2)
