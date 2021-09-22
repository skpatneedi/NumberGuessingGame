import random

x = random.randint(1,9)
chances = 0

while chances < 5:
	chances += 1
	guess = int(input("Guess a number:- "))
	if x == guess:
		print("Congratulations you did it")
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

if not chances < 5 :
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")
