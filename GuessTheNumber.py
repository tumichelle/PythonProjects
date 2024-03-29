#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

i = 0


while i < 3:
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
	else:
		guess = int(guess) # converts a string to an integer
		if int(guess) < aRandomNumber:
			print("Guess higher!")
			i += 1
		if int(guess) > aRandomNumber:
			print("Guess lower!")
			i += 1
		if int(guess) == aRandomNumber:
			print("That's right!")
if i == 3:
	print("You lose! You've used up all your guesses")
