# m(lb) = m(kg) / 0.45359237
# m(kg) = m(lb) × 0.45359237

weight = int(input("Your Weight : "))

unit = input("(L)bs or (K)g : ").lower()

if unit == 'l':
    converted = weight * 0.45
    print(f"Your weight is {converted} bs.")
elif unit == 'k':
    converted = weight / 0.45
    print(f"Your weight is {converted} kg.")

