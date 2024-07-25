# Task 1
# Take in strings of numbers such as "three", "fifty" etc. convert to numbers
# Return value should be integers
number_dict =  number_dict = {
   "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, 
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, 
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, 
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, 
    "twenty": 20, 
    "twenty-one": 21, "twenty-two": 22, "twenty-three": 23, "twenty-four": 24,
    "twenty-five": 25, "twenty-six": 26, "twenty-seven": 27, "twenty-eight": 28,
    "twenty-nine": 29, 
    "thirty": 30, 
    "thirty-one": 31, "thirty-two": 32, "thirty-three": 33, "thirty-four": 34,
    "thirty-five": 35, "thirty-six": 36, "thirty-seven": 37, "thirty-eight": 38,
    "thirty-nine": 39, 
    "forty": 40, 
    "forty-one": 41, "forty-two": 42, "forty-three": 43, "forty-four": 44,
    "forty-five": 45, "forty-six": 46, "forty-seven": 47, "forty-eight": 48,
    "forty-nine": 49, 
    "fifty": 50, 
    "fifty-one": 51, "fifty-two": 52, "fifty-three": 53, "fifty-four": 54,
    "fifty-five": 55, "fifty-six": 56, "fifty-seven": 57, "fifty-eight": 58,
    "fifty-nine": 59, 
    "sixty": 60, 
    "sixty-one": 61, "sixty-two": 62, "sixty-three": 63, "sixty-four": 64,
    "sixty-five": 65, "sixty-six": 66, "sixty-seven": 67, "sixty-eight": 68,
    "sixty-nine": 69, 
    "seventy": 70, 
    "seventy-one": 71, "seventy-two": 72, "seventy-three": 73, "seventy-four": 74,
    "seventy-five": 75, "seventy-six": 76, "seventy-seven": 77, "seventy-eight": 78,
    "seventy-nine": 79, 
    "eighty": 80, 
    "eighty-one": 81, "eighty-two": 82, "eighty-three": 83, "eighty-four": 84,
    "eighty-five": 85, "eighty-six": 86, "eighty-seven": 87, "eighty-eight": 88,
    "eighty-nine": 89, 
    "ninety": 90, 
    "ninety-one": 91, "ninety-two": 92, "ninety-three": 93, "ninety-four": 94,
    "ninety-five": 95, "ninety-six": 96, "ninety-seven": 97, "ninety-eight": 98,
    "ninety-nine": 99, 
    "one hundred": 100
}
def wordToNum():
   word = input("enter a numeric word. ",)
   if word in number_dict:
        number = number_dict[word]
        print(f"{word} as an integer is {number}.")
   else:
       print("enter a number between one and a hundred.")
wordToNum()

# I know this conversion is very basic and flawed. I found it very difficult to determine which loop would be best. My defining of functions is also still very basic.



# Task 2
# Create a program that plays scissors paper rock against the user
# Make the choice of the computer player random
# Consider how a CPU player would pick and how to select the winner
# Hint: In-built modules in python can help you do this task
import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("it's a draw!")
    elif player == "rock" and computer == "scissors":
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("you win!")
    elif player == "scissors" and computer == "paper":
        print("you win!")
    else:
        print("you lose!")
    playAgain = input("play again? (y/n): ").lower()
    if not playAgain == "y":
        running = False
    
print("thanks for playing!")

# Task 3
# In a new repo, start a python environment - install cowsay
# take in user input and return cowsay of the user input