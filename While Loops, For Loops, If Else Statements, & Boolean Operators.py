# WHILE LOOPS, FOR LOOPS, IF ELSE STATEMENTS, & BOOLEAN OPERATORS
#______________________________________________________________________________________________________________________________________________________________________________#
import random

while True:
	user_input = input("Please enter a number between 1 and 10: ") # asks user to enter a number between 1 and 10
	if user_input.isnumeric(): # determines if the user input is all numerical values
		user_inputint = int(user_input) # changes user input string into an int
		if user_inputint <= 10 and user_inputint >= 1: # determines if the user input is less than or equal to 10
			num = random.randint(1,10) # chooses a random int between 1 and 10
			print(f"Your input is equal to the secret number: {user_inputint == num}") # determines if user input is equal to secret number
			print(f"Your input is not equal to the secret number: {user_inputint != num}") # determines if user input is not equal to secret number
			print(f"Your input is greater than the secret number: {user_inputint > num}") # determines if user input is greater than secret numer
			print(f"Your input is less than the secret number: {user_inputint < num}") # determines if user input is less than secret number
			print(f"The secret number is even: {num%2 == 0}") # determines if secret number is even
			guess = input("Please enter your guess for the secret number between 1 and 10: ") # asks user to enter a guess for the secret number between 1 and 10
			if guess.isnumeric(): # determines if the user input is all numerical values
				guess = int(guess) # changes user input string into an int
				if guess <= 10 and guess >= 1: # determines if user input is less than or equal to 10
					print(f"Your guess was {guess == num}, the secret number was {num}") # tells user if guess was correct and the value of the secret number 
					for i in range(num): # prints numers up to but not equal to num
						print(i)
					response = input("Play again? ") # asks user if they want to play again
					if response == "y" or response == "yes" or response == "Yes" or response == "yes" or response == "YES": # accepted user responses
						continue # continue through while loop
					else:
						break # breaks while loop
				else:
					print("Your number was not between 1 and 10") # tells user that number was not between 1 and 10
			else:
				print("Invalid type") # tells user that input was invalid

		else:
			print("Your number was not between 1 and 10") # tells user that number was not between 1 and 10
	else:
		print("Invalid type") # tells user that input was invalid


for i in range (1,11): # prints numbers 1 - 10
	print(i)

for i in "abc": # prints letters a - c
	print(i)
#______________________________________________________________________________________________________________________________________________________________________________#
