# Apart from lists and dictionaries there are another
# two datatypes available in python - these are the set and tuple

# Tuples are an immutable data type - similar to
# a List, except that the contents of a tuple cannot be changed
# This is useful for protecting data from change in a program
# Since no other parts of the code can accidentally change it

# Defining a tuple
tupleVariable = ("cat", "dog", "bort", "the dud", "ratboy")
# Access tuple data similar to list
print(tupleVariable[1])
print(tupleVariable[-1])
print(tupleVariable[2:])  # fetch all results from index 2 to the end
print(tupleVariable[:3])  # fetch all results from beginning to but not including index 3
print(tupleVariable[1:3])  # fetch all results from index 1 to but not including index 3

# Sets are unstructured data within python
# Items defined in sets are not returned the same every time they are printed
# Sets also do not bother with repetition of data - meaning the data
# automatically ignores duplicates
# Define set
setVariable = {"Jeff", "Bob", "Alice"}
myIncorrectSet = {"Jeff", "Jeff", "Bob"}
print(f"Jeff is repeated in this set but it only outputs: {myIncorrectSet}")
# Notice that the output of this print does no display Jeff twice, because it is a repeated value


# Sets are useful when you don't care about the content so much as
# using the data for comparisons

# Sets allow us to compare data and find the similar data or the difference of data

myFriends = {"Alex", "Tom", "Brendan", "Cam"}
onHoliday = {"Alex", "Brendan"}

# Here we can compare our set data and figure out which
# of our friends are available
invitedToTheParty = myFriends.difference(onHoliday)
print(f"These friends are free: {invitedToTheParty}")
# Using the .difference() method python returns the difference of our sets
