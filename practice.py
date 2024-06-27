def plusNumbers (num1, num2):
    return num1+num2

def fullName(firstName, lastName):
    return "Your name is: " + firstName + lastName

def fuckTom():
    return "Fuck Tom"
print(fuckTom())
usersFirstName=input("What is your first name? ")
usersLastName=input("What is your last name? ")

print(fullName(usersFirstName, usersLastName))

num1=input("What number?")

num1=int(num1)

print("Your number is", num1)

print("Your outcome is:", plusNumbers(num1, 3))
