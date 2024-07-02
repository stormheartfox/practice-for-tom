# x=True
# ## if statements are used to evaluate whether a query is true or false
# if x == True:
#     print("Yes")
# ## if else statements are used when a variable can be codified to 2 outcomes
# password="kidGorgeous"
# if password != "":
#     print("Checking your password")
#     if password == "kidGorgeous":
#         print("Welcome!")
# else:
#     print("Go home")

# z=True
# ## elif statements are used when you require more than one if before returning
# if z != True:
#     print("It's not true again")
# elif z == "True":
#     print("It's a string")
# else:
#     print("Then it must be true")

# in a function we can exit by taking the values entered
# and comparing them with one another
# functions should finish when they hit a correct if evaluation
# otherwise they will just keep going until hitting a return

def doesDiCaprioWantMyDaughter(ageOf):
    if ageOf <= 25 and ageOf >= 18:
        return "Leonardo would date your daughter!"
    else:
        return "Sorry Leonardo doesn't want her"

print(doesDiCaprioWantMyDaughter(17))
print(doesDiCaprioWantMyDaughter(26))
print(doesDiCaprioWantMyDaughter(21))

# Write a function that compares whether an animal can be a pet or not
# Accept user input of a pet name & compare the string against values in if statements
# Remember if elif & else - and remember to exit the function on success

# function what animal?
# if bunny - it's allowed
# if dog - it's allowed
# elephant - it's allowed
# if elephant: what country are you in? if country Thailand then yes else no
# else any other is not allowed
def isMyAnimalAPet(animal):
    if animal == "rabbit":
        return "you have a pet!"
    else:
        return "sorry, no dice!"

isMyAnimalAPet("rabbit")
isMyAnimalAPet("tiger")


# Conditional loops - lists and objects
# To make reading the outcome of any statements without comparing every single word with hundreds
# of if/else statements, we can iterate(loop) through lists/dictionaries of data
# this means we can check if something exists in our list of animals without having to write
# a statement for every single one, we just add new animals to the list if we need to

# Example in loop

# Sometimes we want to keep doing something until we reach a certain number. These are called While loops
# while x condition is x then continue to do the thing. E.g while floor is dirty, sweep - you stop sweeping once the
# floor is clean and break out of this statement.

# Example while loop
