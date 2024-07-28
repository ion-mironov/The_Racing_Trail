import random



# Dictionary defining opponent classes with their performance values
opponent_classes = {
	'A': {'hp': 600, 'torque': 600},
	'B': {'hp': 500, 'torque': 500},
	'C': {'hp': 350, 'torque': 350},
	'D': {'hp': 200, 'torque': 200},
}



class Player:
	def __init__(self):
		self.money = 1000		# Initial money
		self.car_hp = 166		# Initial horsepower
		self.car_torque = 159	# Initial torque


	def add_money(self, amount):
		self.money += amount


	def subtract_money(self, amount):
		if self.money >= amount:
			self.money -= amount
			return True
		return False


	def update_car_performance(self, hp_increase, torque_increase):
		self.car_hp += hp_increase
		self.car_torque += torque_increase


	def calculate_win_probability(self, opponent_hp, opponent_torque):
		# Calculate performance difference
		hp_difference = self.car_hp - opponent_hp
		torque_difference = self.car_torque - opponent_torque

		# Example formula: Adjust as needed
		win_probability = 0.5 + (hp_difference + torque_difference) / (2 * max(self.car_hp, opponent_hp))

		# Ensure probability is between 0 and 1
		win_probability = max(0, min(1, win_probability))

		return win_probability


	def race(self, opponent_class):
		# Get opponent's performance values
		opponent_hp = opponent_classes[opponent_class]['hp']
		opponent_torque = opponent_classes[opponent_class]['torque']

		# Calculate win probability
		win_probability = self.calculate_win_probability(opponent_hp, opponent_torque)

		# Simulate the race outcome
		race_result = random.random() < win_probability

		if race_result:
			print("You won the race!")
		else:
			print("You lost the race!")

		return race_result


# Create a global player instance
player_instance = Player()
