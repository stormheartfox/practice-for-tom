# A list (sometimes called array) is a collection of data types separated by commas
# and contained within brackets

myRandomList = ["strings", 123, True, False, 2.5, ["another list inside the list"]]

# You can put anything within the list and access it with a for loop, or with the index
# of the thing you need within the list
# Counting in python begins at 0. So "strings" is at index 0

print(f"Index 0 is {myRandomList[0]}")

# to retrieve the final item in a list we use the index [-1]
print(f"The last item in the list is {myRandomList[-1]}")

# If we want to list each item sequentially we can use a for loop, for x in list 
# do this thing( in this case print)

for listItem in myRandomList:
    print(listItem)

# to retrieve the index of a list item we have to modify our for loop slightly
# .index() is a method that can be applied to lists and dictionaries to find the index
# of a listed item, if it is needed for operations 
for listedItem in myRandomList:
    print(myRandomList.index(listedItem))


# Dictionary

# A dictionary is a data type that holds more detailed and nested information
# this is stored in pairs. Called key-value pairs. The key is the name of the attribute
# the value is the attribute itself.
# e.g  "color": "red" - color is the key, red is the value
# dictionaries are contained in {} called curly braces and key value pairs are 
# separated by commas - all keys must be in "" but values can be any data type

mySimpleDict={
    "color": "red",
    "shade": "dark",
    "code": 250,
    "in stock": False
}

# Similar to lists we can print our dictionary key value pairs with for loops & in-built
# python methods such as .get() & .keys()

for thing in mySimpleDict:
    print(f"{thing} is a key in your dictionary")
    print(f"{mySimpleDict.get(thing)} is the value of the key")

print(mySimpleDict.keys()) # retrieves the keys as a list from the dictionary
