# Homework 2 - writing functions

# Task 1
# Write a function that accepts 2 integers and an if statement that compares them
# if they match - print they match, if they don't print that they don't match
def checkNumbers():
    num1 = int(input ("pick a number "))
    num2 = int(input ("pick another number  "))

    if num1 == num2:
        return " Morbo says your numbers match!"
    else:
        return " Your numbers do not match. Morbo IS dead!"

result = checkNumbers()
print(result)

# Task 2
# Write a function that accepts a list and uses a for loop to print out all of the items in the list
plantList = ["chinese fir", "elephant ear", "money plant", "spider plant"]
for plant in plantList:
    print("I require immediate photosynthesis to survive!")
# Task 3
# write a for loop that prints out the indexes of your list in your function
for plant in plantList:
    print(plantList.index(plant))
# Task 4
# Create a dictionary of cars and trucks, put 2 cars and 2 trucks in each 
MotorVehicleDict = {
    "trucks": {
        "truck1": {
            "roadTrain": False,
            "wheels": 10
        },
    
        "truck2": {
            "roadTrain": True,
            "wheels": 18
        }
    },
    "cars": {
        "car1": {
            "4wheeldrive": True,
            "colour": "blue"
        },
        "car2": {
            "4wheeldrive": False,
            "colour": "green"
        }
    }
}


# Task 5
# create a list of every data type
everyListEveryWhereAllatOnce = ["g string", True, False, 4.5, 96, ["second list"]]

# Task 6
# write a while loop that counts to 10
counter = 1
while counter < 11:
    print(counter)
    counter = counter + 1




# Task 7
# write a function that accepts 2 numbers and an operator and performs a math operation
# based on which operator is given to the function
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
result = calculate(9, 7, '+')
print(result)