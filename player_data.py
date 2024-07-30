class Player:
	def __init__(self):
		self.money = 1000		# Initial money
		self.car_braking = 140	# Initial braking distance in ft from 60 mph
		self.car_hp = 166		# Initial horsepower
		self.car_torque = 159	# Initial torque
		self.car_accel = 10		# Initial 0-60 time in seconds

	def add_money(self, amount):
		self.money += amount

	def subtract_money(self, amount):
		if self.money >= amount:
			self.money -= amount
			return True
		return False

	def update_car_performance(self, braking_distance, hp_increase, torque_increase, accel_decrease):
		self.car_braking -= braking_distance
		self.car_hp += hp_increase
		self.car_torque += torque_increase
		self.car_accel -= accel_decrease


# Create a global player instance
player_instance = Player()
