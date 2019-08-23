import random
start = "Welcome to Michelle's Hangman game."
print(start)

#List of potential words
potential_words = ["chandelier",
"temperature",
"characteristic",
"thimble",
"thunderstorm",
"generation",
"matchmaker",
"drawbridge",
"jealousy",
"tsunami"]

#Choose random word and turn it into a list
word = list(random.choice(potential_words))
NumberOfCharacters = len(word)

#Making list current_word which is printed
#with number of blanks same as number of characters
current_word = ["_"]
for i in range(NumberOfCharacters - 1):
	current_word.append("_")

print(*current_word)

guesses = []
maxfails = 10
fails = 0

guess = input("Guess a letter: ")

while fails + 1 < maxfails:
	if (guess.isalpha()) == False:
		print("That's not one letter")
	if (guess in guesses) == True:
		print("You've already guessed that letter.")
	if (guess in guesses) == False:
		if ("_" in current_word) == True:
			if (guess in word) == True:
				print("Nice! That is in the word.")
				for i in range(len(word)):
					if word[i] == guess:
						current_word[i] = guess
			if (guess in word) == False:
				print("That letter is not in the word.")
				fails = fails + 1
		if ("_" in current_word) == False:
			break
	guesses.append(guess)
	print(*current_word)
	print("You have " + str(maxfails - fails) + " tries left!")
	guess = input("Guess again!")

if "_" in current_word == False:
	print("Congratulations! You have guessed the right word.")


# check if the guess is valid: Is it one letter? Have they already guessed it?

# check if the guess is correct: Is it in the word? If so, reveal the letters!

if fails == maxfails:
	print("Sorry, you're out of tries")
