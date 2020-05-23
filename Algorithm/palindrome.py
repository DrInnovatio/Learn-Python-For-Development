def palindrome(s):
    queue = []
    stack = []

# isalpha() is a built-in method used for string handling.
# isalpha() does not take any parameters

    for x in s:
        if x.isalpha():
            queue.append(x.lower())
            stack.append(x.lower())

    while queue:
        if queue.pop(0) != stack.pop():
            return False

    return True

print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))