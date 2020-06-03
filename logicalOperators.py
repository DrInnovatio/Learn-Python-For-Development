# AND : Both should be true.
# OR : at least one should be true.

has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print("You are eligible for the loan")

# Conditions

name = "John Park"

if len(name) < 3:
    print("Name must be at least three characters.")
elif len(name) > 20:
    print("The name is too long!")
else:
    print("The name looks good.")
