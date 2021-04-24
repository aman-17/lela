from classes.User import User

class Report(object):

	# Initial value for id number
	# For each report add increment the id by 1
	count = 4000
	users = []

	def __init__(self, users_array, user_index, meal_report):
		self.report_id = Report.count
		Report.users = users_array
		self.user_index = user_index
		self.meal_report = meal_report
		Report.count += 1
	
	def printToFile(self):
		text = ""
		user = Report.users[self.user_index]
		if user.gender == 'm':
			gender = "Male"
		else:
			gender = "Female"
		text += "\nREPORT" + "\n\n"
		
		text += "USER DETAILS\n\n"
		
		text += "Name           : " + user.user_name + "\n"
		text += "Age            : " + str(user.age) + "\n"
		text += "Gender         : " + gender + "\n"
		text += "Height         : " + str(user.height) + "cm\n"
		text += "Weight         : " + str(user.weight) + "kg\n"
		text += "Weight Goal    : " + str(user.weight_goal) + "kg\n"
		
		text += "Your BMI is " + str("%.1f" % user.getBMI()) + " and your weight status is " + user.getBMIStatus() + "\n\n"
		text += "CALORIES REPORT\n"
		
		text += "Daily calories you need to maintain your current weight is " + str("%d" % user.getDailyCalories()) + "\n"
		diff = user.getWeightDiff()
		daily_calories_change = user.getCaloriesChange()
		if diff < 0:
			text += "Daily calories you need to lose weight (" + str("%.2f" % abs(diff)) + "kg/week) is " + str("%d" % daily_calories_change) + "\n"
		elif diff > 0:
			text += "Daily calories you need to gain weight (" + str("%.2f" % abs(diff)) + "kg/week) is " + str("%d" % daily_calories_change) + "\n"
		text += "\nSUGGESTED MEAL\n\n"
		
		text += self.meal_report + "\n"

		file_path = "files/reports.txt"
		file = open(file_path, "a")
		file.write(text)

		file_path = "user_reports/" + user.user_name.replace(" ", "_") + "_diet_report.txt"
		file = open(file_path, "w")
		file.write(text)
		#print("Full diet report successfully generated. Please check folder 'user_reports'.\n")

