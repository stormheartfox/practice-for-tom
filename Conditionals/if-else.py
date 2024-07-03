# if statements are used to evaluate whether a query is true or false
# example:
# x=True
# if x == True:
#     print("Yes")
# This will print yes because x == True is a true statement.


# By taking values and evaluating them with if statements we can do 
# different actions - if you're over 18 for example you can enter a pub
# functions should return(finish) when they hit a correct if evaluation
# otherwise they will just keep going until hitting a return

# In this example we give our function an ageOf our daughter, then evaluate whether
# Leonardo DiCaprio will date them by asking if they are over 18 but below the age
# of 25

def doesDiCaprioWantMyDaughter(ageOf):
    if ageOf <= 25 and ageOf >= 18:
        return "Leonardo would date your daughter!"
    else:
        return "Sorry Leonardo doesn't want her"

# Here 17 evalutes to false because it is below 25 but also below 18
# so 1 statement is true and the other is false - so the outcome is false
print(doesDiCaprioWantMyDaughter(17))
print(doesDiCaprioWantMyDaughter(26))
print(doesDiCaprioWantMyDaughter(21))
# 21 evaluates as true because it passes the test of below 25 and above 18

# here is a list of animals & we check to see if the animal is in the list
# before we determine that it's a pet! if it's not in the list we print
# sorry no dice to the user
animalList = ["rabbit","tiger","snake","elephant", "cat", "dog"]


def isMyAnimalAPet(animal):
    if animal in animalList:
        return "you have a pet!"
    else:
        return "sorry, no dice!"


yourAnimal=input("What is your animal?")

print(isMyAnimalAPet(yourAnimal))



# Conditional loops - lists and dictionaries
# To make reading the outcome of any statements without comparing every single word with hundreds
# of if/else statements, we can iterate(loop) through lists/dictionaries of data
# this means we can check if something exists in our list of animals without having to write
# a statement for every single one, we just add new animals to the list if we need to


# If we have many if statements, we can use elif in the space between our first if and our
# final else statement - e.g if this == this do x elif this == that do y else do z

multipleIfsTest="bongo"

if multipleIfsTest == "bingo":
    print("bingo!")
elif multipleIfsTest == "bango":
    print("bango")
else:
    print("bongo!")
