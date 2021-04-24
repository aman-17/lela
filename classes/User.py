import math

class User(object):

	# Initial value for id number
	# For each user add increment the id by 1
	count = 1000

	def __init__(self, user_name, age, gender, height, weight, weight_goal, activity_level):
		
		self.user_name = user_name
		self.age = int(age)
		self.gender = gender
		self.height = int(height)
		self.weight = int(weight)
		self.weight_goal = float(weight_goal)
		self.activity_level = int(activity_level)
		self.count += 1

	def printUserDetails(self):
		
		if self.gender == 'm':
			gender = "Male"
		else:
			gender = "Female"
		print(
		"Name           : " + self.user_name + "\n"
		"Age            : " + str(self.age) + "\n"
		"Gender         : " + gender + "\n"
		"Height         : " + str(self.height) + "cm\n"
		"Weight         : " + str(self.weight) + "kg\n"
		"Weight Goal    : " + str(self.weight_goal) + "kg\n")
		

	def getBMI(self):
		
		height = self.height/100 
		return self.weight/(height*height)

	def getBMR(self):
		
		if self.gender == 'm':
			return math.ceil(66 + (13.7 * self.weight) + (5.0 * self.height) - (6.8 * self.age))
		elif self.gender == 'f':
			return math.ceil(655 + (9.6 * self.weight) + (1.8 * self.height) - (4.7 * self.age))
		else:
			return 0

	def getDailyCalories(self):
		bmr = self.getBMR()
		if self.activity_level == 1: 
			return math.ceil(bmr * 1.2)
		elif self.activity_level == 2:
			return math.ceil(bmr * 1.375)
		elif self.activity_level == 3:
			return math.ceil(bmr * 1.55)
		elif self.activity_level == 4:
			return math.ceil(bmr * 1.725)
		elif self.activity_level == 5:
			return math.ceil(bmr * 1.9)
		else:
			return 0

	def getBMIStatus(self):
		bmi = self.getBMI()
		
		if bmi < 18.5: return "Underweight"
		elif bmi >= 18.5 and bmi < 25.0: return "Normal"
		elif bmi >= 25.0 and bmi < 30.0: return "Overweight"
		else: return "Obese"
		"""
		Below 18.5	Underweight
		18.5 – 25.0	Normal
		25.0 – 30.0	Overweight
		30.0 – 35.0	Class 1 Obese
		35.0 – 40.0	Class 2 Obese
		Above 40.0	Class 3 Obese

		"""
	def getCaloriesChange(self):
		weight_diff = self.getWeightDiff()
		calories_diff = weight_diff * 1000
		daily_calories = self.getDailyCalories()
		return daily_calories + calories_diff

	def getWeightDiff(self):
		return self.weight_goal - self.weight
