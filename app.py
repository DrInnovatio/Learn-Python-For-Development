birth_year = input("Birth year : ")
age = 2020 - int(birth_year)
print("You are ", age, "years old.")

# To check the data type

birth_year = input("Birth year : ")
print(type(birth_year))
age = 2020 - int(birth_year)
# birth_year should be changed into int type to calculate numbers.
print(type(age))
print("You are ", age, "years old.")

# Question
# Ask a user their weight( in pounds ), convert it to kilograms and print on the terminal.

pounds = input("What is your weight in pounds ? : ")
kilo = float(0.45 * float(pounds))
print("Your weight is ", kilo, " kilogram.")

# Writing multiful lines between ''' and '''

email = ''' 
Hello John.
Here is our first email to you.
Support Team.
'''

print(email)