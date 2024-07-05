# In python, as with all programming languages there are a number of operators.
# These are shared & used generally the same across all programming languages

# Arithmetic Operators

#  + used for addition
print("Addition:",5+5) # 10
#  - used for subtraction
print("Subtraction:",5-5) # 0
#  * used for multiplication
print("Multiplication:",5*5) # 25
#  / used for division (returns a float)
print("Division:",5/5) # 1.0
# // used for floor division (Rounding down to the nearest whole integer)
print("Floor Division:",7//2) # 3 (3.5 rounded down)
#  % used for modulo operators (Gives the remainder of integers)
print("Modulo:",7%5) # 2 (5 fits into 7 once and remainder 2)
# ** used for for exponentiation (To the power of any integer)
print("Exponentiation:",10**2) # 100 (10 times itself)

# Assignment Operators
# The primary assignment operator is = 
# this can be modified with arithmetic operators as a short hand for adding numbers
# to an already declared number

# Initial assignment =
initialVariable=1
print(f"Initial assignment: {initialVariable}") # 1
# Plus initial assignment
initialVariable+=1 # 2
print(f"Initial assignment += 1: {initialVariable}")
initialVariable+=3
print(f"Initial assignment += 3: {initialVariable}") #5
# Any uses of the initial variable += adds to the count in the program updating the initial 
# variable with the value + the new number
# The same can be done with other operators such as subtraction, multiplication etc.
initialVariable*=5
print(f"Initial assignment *= 5: {initialVariable}") # 25
initialVariable-=5
print(f"Initial assignment -= 5: {initialVariable}") # 20
# The value has now added up to 5, then multiplied by 5 and then subtracted 5

# Equivalancy operators
# These operators compare values & return a True or False boolean
# Generally these are used in if statements & loops

# The == does a direct comparison of values, they must be exactly a like to return True
print(f"Compare if cat is cat: {'cat'=='cat'}") # True
print(f"Compare if cat is dog: {'cat'=='dog'}") # False

# The != compares if values are NOT equal to one another and returns True if they DON'T match
print(f"Compare if cat is not equal to dog: {'cat'!='dog'}") # True they aren't the same
print(f"Compare if cat is not equal to cat: {'cat'!='cat'}") # False they are the same

# Greater than
print(f"3 is greater than 2: {3>2}") # True
# Less than 
print(f"3 is less than 2: {3<2}") # False
# Greater than or equal to
print(f"3 is greater than or equal to 3: {3>=3}") # True
# Less than or equal to
print(f"3 is less than or equal to 3: {3<=3}") # True

# Logical Operators
# Used to combine statements when doing comparisons

# And operator
# All statements seperated by and must be true to return true. 
# If either is false, False is returned
print(f"cat equals cat AND 3 equals 3: {'cat'=='cat' and 3==3}") # True
print(f"cat equals cat AND 3 equals 2: {'cat'=='cat' and 3==2}") # False
# Or operator
# Any of the statements separated by or must be true to return True
# If all statements are false, False is returned
print(f"cat equals cat OR 3 equals 2: {'cat'=='cat' or 3==2}") # True
print(f"cat equals dog OR 3 equals 2: {'cat'=='dog' or 3==2}") # False
# Not operator
# Essentially the same as != not equal to returns true if something is
# not equal and false if they are equal
# not and is not are essential the same but expressed slightly differently
print(f"Compare if cat is not equal to dog: {'cat'is not'dog'}") # True they aren't the same
print(f"Compare if cat is not equal to cat: {'cat'is not'cat'}") # False they are the same
print(f"Compare if cat equal dog is not true: {not('cat'=='dog')}") # True they aren't the same
print(f"Compare if cat equal cat is not true: {not('cat'=='cat')}") # False they are the same

# Is operator
# Essentially the equivalent to == operator
# Returns True if the values are the same
print(f"Compare if cat is cat: {'cat'is'cat'}") # True
print(f"Compare if cat is dog: {'cat'is'dog'}") # False