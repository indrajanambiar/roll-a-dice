"""
#dice rolling game
> crete a program that accepts a total number of rolls (N) from the user
> make N rolls and output the sum	
> eg: create a random choice
	 if __name__ == "__main__":

improvements
>>>
accept the number of users playing M
accept their names
roll dice N times for each player and output the winner

"""

import random
import time
from random import randint
N = 3

def game():
	m=int(input("number of players"))
	print('number of players is:',m)
	names = list()
	scores = list()

	for i in range(m):
		name= input("enter player name:")
		names.append(name)
	for name in names:
		score = get_user_input(name)
		scores.append(score)

	max_score = max(scores)
	winner = names[scores.index(max_score)]
	print('winner is :',winner)


def get_user_input(name):	
	print(f"Let's get to rolling, {name}!")
	score = roll_n_times(N)
	print(f"FINAL SCORE for {name} is", score)
	return score

def roll_dice():
	"""
	roll dice once and return the result 
	"""
	return random.choice(range(1, 7))

def roll_n_times(n):
	sum = 0
	for i in range(n):
		print("\nrolling dice.....")
		roll_value =  roll_dice()
		print(f"you got a: {roll_value}")
		sum = sum + roll_value
	return sum	

if __name__ == "__main__":
	game()