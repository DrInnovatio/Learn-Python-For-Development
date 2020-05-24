def find_same_name(a):

    name_dict = {}
    for name in a :
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1

# Set, a term in mathematics for a sequence consisting of distinct language
# is also extended in its language by Python and can easily be made using set().

    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result


name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))

name2 = ["Tom", "Jerry", "Mike", "Bill", "Bill", "Jane"]
print(find_same_name(name2))