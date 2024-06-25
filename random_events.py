import random

def random_event():
	events = [
		"You found an abandoned car with a useful part!",
		"You found a cache of money!",
		"Your car has a flat tire!",
		"Your engine is overheating!",
	]
	return random.choice(events)