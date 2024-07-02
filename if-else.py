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

import string


def doesDiCaprioWantMyDaughter(ageOf):
    if ageOf <= 25 and ageOf >= 18:
        return "Leonardo would date your daughter!"
    else:
        return "Sorry Leonardo doesn't want her"

# print(doesDiCaprioWantMyDaughter(17))
# print(doesDiCaprioWantMyDaughter(26))
# print(doesDiCaprioWantMyDaughter(21))

# Write a function that compares whether an animal can be a pet or not
# Accept user input of a pet name & compare the string against values in if statements
# Remember if elif & else - and remember to exit the function on success

# function what animal?
# if bunny - it's allowed
# if dog - it's allowed
# elephant - it's allowed
# if elephant: what country are you in? if country Thailand then yes else no
# else any other is not allowed
animalList = ["rabbit","tiger","snake","elephant", "cat", "dog"]

for animal in animalList:
    print(animal)

print(animalList[0])
print(animalList[3])
print(animalList[-1])

def isMyAnimalAPet(animal):
    if animal in animalList:
        return "you have a pet!"
    else:
        return "sorry, no dice!"


# yourAnimal=input("What is your animal?")

# print(isMyAnimalAPet(yourAnimal))

ourAnimal = {
    "breed": "dalmation",
    "legs": 4,
    "disabled": False
}
animalShelterAnimals = {
    "cats": {
        "cat1": {
            "breed": "tabby",
            "legs": 0
        },
        "cat2": {
            "breed": "shorthair",
            "legs": 2,
            "wheels": 2
        }
        },
    "dogs": {
        "dog1": {
            "breed": "tabby",
            "legs": 6
        }
    },
    "pigs": {
        "pig1":{
            "weight": 500,
            "measurement": "lbs"
        }
    }
}

for animalType in animalShelterAnimals:
        print("This is the animal type", animalType)

print(animalShelterAnimals.get("cats").get("cat1"))
# Data Types
# int 2
# bool True False
# list [1,2,]
# dict {"key":"value"}
# string "words"

# Conditional loops - lists and dictionaries
# To make reading the outcome of any statements without comparing every single word with hundreds
# of if/else statements, we can iterate(loop) through lists/dictionaries of data
# this means we can check if something exists in our list of animals without having to write
# a statement for every single one, we just add new animals to the list if we need to

# Example in loop

# Sometimes we want to keep doing something until we reach a certain number. These are called While loops
# while x condition is x then continue to do the thing. E.g while floor is dirty, sweep - you stop sweeping once the
# floor is clean and break out of this statement.

# Example while loop


# while stadium empty let people in

fullStadium=5
currentOccupants=0
while currentOccupants < fullStadium:
    print("You may enter")
    currentOccupants += 1


# write a function that tells you to eat until you're full

# function - def doIEat():
# while i'm not full keep eating
stomachIsEmpty = True
maxCalories = 2000
calories = 0
while stomachIsEmpty:
    if calories >= maxCalories:
        stomachIsEmpty=False
        print("Please stop eating")
        print(calories)
    else:
        print("eat more food")
        calories+=200

