# Python Homework 1
# Complete these tasks and push them 
# to github for review

# Task 1: Print your name in the command line:
print("Thomas Pringle")


# Task 2: Create 3 variables - one string - one integer - one boolean:
#string 1
message = """
We meet again Mad Magazine
only our momentary lapse of concentration allowed Charlie to get the drop on us.
"""
print(message)
#integer1
x = int(39)
print(x)
#bool1
x = "Michael Velsigne"
y= "Nowra climbing"
print(bool(x))
print(bool(y))
# Task 3: Print your 3 variables to the command line:
#see above


# Task 4: Create a function that accepts 1 argument & returns the argument
def greet():
    print("Hello! I haven't seen you in ages! ")
    userResponse=input("How have you been? ")
    if userResponse == "very well, thank you!":
        print("glad to hear it!")
        return
greet()
# Task 5: Print the return of your function to the command line:
# note: you must give the function 1 argument for it to print


# Task 6: Ask the user what their name is in the command line:
def fullName(firstName, lastName):
    return "Your name is: " + firstName + lastName
usersFirstName=input("What is your first name? ")
usersLastName=input("What is your last name? ")



# Task 7: Print the "Your name is : " and the users name into the command line:
#see above
print(fullName(usersFirstName , usersLastName))

# Task 8: Define a function that multiplies 2 numbers:
def multiply(a, b):
    
    return a * b
result = multiply(10, 12)
print("the product is", result)


# Task 9: Ask the user for 2 numbers (store them in variables)
num1 = int(input("Enter a number: "))
print("The entered number is:", num1)

num2 = int(input("Enter a second number: "))
print("The entered number is:", num2)


# Task 10: Use your multiplier function to calculate the result of the users 2 numbers
# note: the numbers have not been converted to int() make sure to convert the users input
num3 = int(num1 * num2)

# Task 11: Print the return of the multiplication to the command line:
print("The result of the multiplication of your numbers is", num3)


# Bonus Tasks
# The following tasks require you to google how to write the code
# TASK 12: Ask the user for a number & convert their number to an integer
# Write an IF STATEMENT that prints "Your number is larger than 3" if
# the user gives a number GREATER THAN 3


num = int(input("Enter an integer: "))
if num >3: print("your number is larger than 3.")





# TASK 13: Write an if statement that prints "Your number is lower than 3"
# if the user gives a number LESS THAN 3 

if num <3: print("your number is lower than 3.")