from os import abort
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, send_file
from flask_login import login_required, current_user
from flask.globals import session
import json
#from app import app
from classes.User import User
# from . import getSuggestedMeal, normal_user_view

import time
import os
import math
from classes.User import User
from classes.Report import Report
from classes.Food import Food

views = Blueprint('views',__name__,template_folder="templates/")

@views.route('/', methods=['GET','POST'])
# @login_required
def mainpage():
    
    return render_template("mainpage.html", user=current_user) 

@views.route('/enterdetails', methods=['GET', 'POST'])
#@login_is_required
def enterdetails():
    
    if request.method == 'POST':
    
        user_name = request.form.get('user_name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        height = request.form.get('height')
        weight = request.form.get('weight')
        weight_goal = request.form.get('goal')
        activity_level = request.form.get('activity')
        nonveg = request.form.get('nonveg')
        
        result1=normal_user_view(user_name, age, gender, height, weight, weight_goal, activity_level,nonveg)
    
        if gender == 'f' or gender == 'm'  :
            return render_template("report.html",user_namehtml=result1[0],agehtml=result1[1],genderhtml=result1[2], 
                                   heighthtml=result1[3],weighthtml=result1[4], weight_goalhtml=result1[5],
                                   bmihtml=result1[6], bmi_statushtml=result1[7], dailycalorieshtml=result1[8],
                                   daily_calories_changehtml=result1[9], mealreport0html=result1[10],
                                   mealreport1html=result1[11], mealreport2html=result1[12],
                                   tmealreport0html=result1[13], tmealreport1html=result1[14] ,tmealreport2html=result1[15],
                                   grandmealreporthtml=result1[16], user=current_user)

        else:
            flash("Enter correct details", category='error')
        

    return render_template("enterdetails.html", user=current_user)

@views.route('/login', methods=['GET','POST'])
# @login_required
def login():
    
    return render_template("login.html", user=current_user)   

@views.route('/about', methods=['GET','POST'])
# @login_required
def about():
      
    return render_template("about.html", user=current_user)
   
@views.route('/recipe', methods=['GET','POST'])
# @login_required
def recipe():
    
    return render_template("recipe.html", user=current_user)

@views.route('/logoutbutton', methods=['GET','POST'])
# @login_required
def logoutbutton():
       
    return render_template("logoutbutton.html", user=current_user)

@views.route('/index', methods=['GET','POST'])
# @login_required
def index():
   
    
    return render_template("index.html", user=current_user)

@views.route('/reportdownload', methods=['GET','POST'])
# @login_required
def reportdownload():
   
    return send_file('/home/aman17/Flask-Web-App/user_reports/Aman_diet_report.txt')

@views.route('/parentalpregnancy', methods=['GET','POST'])
def f_parentalpregnancy():
   
    return render_template("f_parentalpregnancy.html", user=current_user)

@views.route('/f_home', methods=['GET','POST'])
def f_home():
   
    return render_template("f_home.html", user=current_user)
    
@views.route('/f_about', methods=['GET','POST'])
def f_about():
   
    return render_template("f_about.html", user=current_user)

@views.route('/f_gym', methods=['GET','POST'])
def f_gym():
   
    return render_template("f_gym.html", user=current_user)

@views.route('/f_contact', methods=['GET','POST'])
def f_contact():
   
    return render_template("f_contact.html", user=current_user)

@views.route('/h_index', methods=['GET','POST'])
def h_index():
   
    return render_template("h_index.html", user=current_user)

@views.route('/h_abouthealth', methods=['GET','POST'])
def h_abouthealth():
   
    return render_template("h_abouthealth.html", user=current_user)


@views.route('/h_gallery', methods=['GET','POST'])
def h_gallery():
   
    return render_template("h_gallery.html", user=current_user)

@views.route('/h_events', methods=['GET','POST'])
def h_events():
   
    return render_template("h_events.html", user=current_user)

@views.route('/h_lifestyle', methods=['GET','POST'])
def h_lifestyle():
   
    return render_template("h_lifestyle.html", user=current_user)

@views.route('/h_wellness', methods=['GET','POST'])
def h_wellness():
   
    return render_template("h_wellness.html", user=current_user)

@views.route('/h_allergies', methods=['GET','POST'])
def h_allergies():
   
    return render_template("h_allergies.html", user=current_user)

@views.route('/h_weightloss', methods=['GET','POST'])
def h_weightloss():
   
    return render_template("h_weightloss.html", user=current_user)

@views.route('/h_pregnancy', methods=['GET','POST'])
def h_pregnancy():
   
    return render_template("h_pregnancy.html", user=current_user)

@views.route('/h_diseases', methods=['GET','POST'])
def h_diseases():
   
    return render_template("h_diseases.html", user=current_user)

@views.route('/h_gal_sub_health', methods=['GET','POST'])
def h_gal_sub_health():
   
    return render_template("h_gal_sub_health.html", user=current_user)

@views.route('/h_gal_sub_sports', methods=['GET','POST'])
def h_gal_sub_sports():
   
    return render_template("h_gal_sub_sports.html", user=current_user)

@views.route('/h_gal_sub_lifestyle', methods=['GET','POST'])
def h_gal_sub_lifestyle():
   
    return render_template("h_gal_sub_lifestyle.html", user=current_user)

@views.route('/h_gal_sub_environment', methods=['GET','POST'])
def h_gal_sub_environment():
   
    return render_template("h_gal_sub_environment.html", user=current_user)

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)
        else:
            return function()
    return wrapper




def normal_user_view(user_name, age, gender, height, weight, weight_goal, activity_level, nonveg):
    users.append(User(user_name, age, gender.lower(), height, weight, weight_goal, activity_level))
    user_index = len(users)-1
    bmi_no = str("%.1f" % users[user_index].getBMI())
    bmi_status = users[user_index].getBMIStatus()
    daily_calories = users[user_index].getDailyCalories()
    daily_calories_change = math.ceil(users[user_index].getCaloriesChange())
    '''
    if diff < 0:
        cal_lose_weight = str("%.2f" % abs(diff))
        cal_change_lose = str("%d" % daily_calories_change)
    elif diff > 0:
        cal_gain_weight = str("%.2f" % abs(diff))
        cal_change_lose = str("%d" % daily_calories_change)
    '''    
    calories_each_meal = daily_calories_change/3
    meal_report = getSuggestedMeal(calories_each_meal,nonveg)
    report_print = meal_report[7]
    
    mealreport0=meal_report[0]
    mealreport1=meal_report[1]
    mealreport2=meal_report[2]
    tmealreport1=meal_report[3]
    tmealreport2=meal_report[4]
    tmealreport3=meal_report[5]
    grandmealreport=meal_report[6]
    r = Report(users, user_index, report_print)
    r.printToFile()
    return user_name, age, gender, height, weight, weight_goal, bmi_no, bmi_status, daily_calories, daily_calories_change, mealreport0, mealreport1, mealreport2, tmealreport1, tmealreport2, tmealreport3, grandmealreport

def getSuggestedMeal(cal,nonveg):
	users = []
	foods = []

	# List for grouping meals
	breakfast = [[0 for x in range(3)] for y in range(8)]
	lunch = [[0 for x in range(3)] for y in range(8)]
	dinner = [[0 for x in range(3)] for y in range(8)]

	# Load database from file

	

	if(nonveg == 'y'):
		reports_file_path = "files/reports.txt"
		users_file_path = "files/users.txt"
		foods_file_path = "files/nonveg.txt"
	else:
		reports_file_path = "files/reports.txt"
		users_file_path = "files/users.txt"
		foods_file_path = "files/veg.txt"

	'''
	if not os.path.exists(reports_file_path):
		print("File '" + reports_file_path + "' is not exists")

	if not os.path.exists(foods_file_path):
		print("File '" + foods_file_path + "' is not exists")
	''' 

	# Read foods data from ext file
	f = open(foods_file_path, "r")
	lines = f.read().splitlines()

		
	count = 0 # foods count
	bc = 0 # bfast count
	lc = 0 # lunch count
	dc = 0 # dinner count
	for y in range(0, int(len(lines)/5)):
		y *= 5
		foods.append(Food(lines[y], lines[y+1], lines[y+2], lines[y+3]))

		#Grouping of type of meals, into specific array
		lastChar = foods[count].meal_type[len(foods[count].meal_type)-1]
		if y/5 == int(len(lines)/5)-1: 
			nxtLastChar = "9"
		else:
			nxtLastChar = lines[y+5][len(lines[y+5])-1]

		if "breakfast" in foods[count].meal_type:
			breakfast[int(lastChar)-1][bc] = count
			if int(nxtLastChar) > int(lastChar): 
				bc = 0
			else:
				bc += 1
		elif "lunch" in foods[count].meal_type:
			lunch[int(lastChar)-1][lc] = count
			if int(nxtLastChar) > int(lastChar):
				lc = 0
			else:
				lc += 1
		else:
			dinner[int(lastChar)-1][dc] = count
			if int(nxtLastChar) > int(lastChar):
				dc = 0
			else:
				dc += 1
		count += 1

	text = ""
	text1 = ""
	text2 = ""
	text3 = ""
	texttotal1 = ""
	texttotal2 = ""
	texttotal3 = ""
	grandtotal = ""
	
	# Breakfast Foods
	minDiff = 9999999
	for i in range(0, len(breakfast)):
		totalCal = 0
		for j in range(0, len(breakfast[i])):
			if (i == 0 and j == 0) or breakfast[i][j]:
				totalCal += float(foods[breakfast[i][j]].calories)
		if abs(totalCal-cal) < minDiff:
			minDiff = abs(totalCal-cal)
			bset = i
			bsetCal = totalCal

	text += "Breakfast:\n"
	for j in range(0, len(breakfast[bset])):
		text += "\n"
		if (bset == 0 and j == 0) or breakfast[bset][j]:
			text1 += str(j+1) + ": " + foods[breakfast[bset][j]].name + ". \n"
			text += "Meal " +str(j+1) + ": " + foods[breakfast[bset][j]].name + ". \n"
			text1 += "Amount: " + foods[breakfast[bset][j]].amount + ". \n"
			text += "Amount: " + foods[breakfast[bset][j]].amount + ". \n"
			text1 += "Calories: " + foods[breakfast[bset][j]].calories + ". \n"
			text += "Calories: " + foods[breakfast[bset][j]].calories + ". \n"
	texttotal1 += "Total Breakfast Calories: " + str("%.1f" % (bsetCal)) + ". \n\n"
	text += "Total Breakfast Calories: " + str("%.1f" % (bsetCal)) + ". \n\n"

	# Lunch Foods
	minDiff = 9999999
	for i in range(0, len(lunch)):
		totalCal = 0
		for j in range(0, len(lunch[i])):
			if (i == 0 and j == 0) or lunch[i][j]:
				totalCal += float(foods[lunch[i][j]].calories)
		if abs(totalCal-cal) < minDiff:
			minDiff = abs(totalCal-cal)
			lset = i
			lsetCal = totalCal

	#text2 += "Lunch:\n"
	for j in range(0, len(lunch[lset])):
		
		if (lset == 0 and j == 0) or lunch[lset][j]:
			text2 += str(j+1) + ": " + foods[lunch[lset][j]].name + ". \n"
			text2 += "Amount: " + foods[lunch[lset][j]].amount + ". \n"
			text2 += "Calories: " + foods[lunch[lset][j]].calories + ". \n"
			text += "Meal " +str(j+1) + "  : " + foods[lunch[lset][j]].name + ". \n"
			text += "Amount: " + foods[lunch[lset][j]].amount + ". \n"
			text += "Calories: " + foods[lunch[lset][j]].calories + ". \n\n"
	texttotal2 += "Total Dinner Calories: " + str("%.1f" % (lsetCal)) + ". \n\n"
	text += "Total Dinner Calories: " + str("%.1f" % (lsetCal)) + ". \n\n"
	# Dinner Foods
	minDiff = 9999999
	for i in range(0, len(dinner)):
		totalCal = 0
		for j in range(0, len(dinner[i])):
			if (i == 0 and j == 0) or dinner[i][j]:
				totalCal += float(foods[dinner[i][j]].calories)
		if abs(totalCal-cal) < minDiff:
			minDiff = abs(totalCal-cal)
			dset = i
			dsetCal = totalCal

	
	for j in range(0, len(dinner[dset])):
		
		if (dset == 0 and j == 0) or dinner[dset][j]:
			text3 += str(j+1) + ": " + foods[dinner[dset][j]].name + ". \n"
			text3 += "Amount: " + foods[dinner[dset][j]].amount + ". \n"
			text3 += "Calories: " + foods[dinner[dset][j]].calories + ". \n"
			text += "Meal " +str(j+1) + ": " + foods[dinner[dset][j]].name + ". \n"
			text += "Amount: " + foods[dinner[dset][j]].amount + ". \n"
			text += "Calories: " + foods[dinner[dset][j]].calories + ". \n\n"
	texttotal3 += "Total Lunch Calories: " + str("%.1f" % (dsetCal)) + ". \n"
	text += "Total Lunch Calories: " + str("%.1f" % (dsetCal)) + ". \n\n"
	totalMealCal = math.ceil(bsetCal + lsetCal + dsetCal)	
	grandtotal += "TOTAL CALORIES: " +str(totalMealCal) + ". \n"
	text += "TOTAL CALORIES: " +str(totalMealCal) + ". \n"	
	return text1, text2, text3, texttotal1, texttotal2, texttotal3, grandtotal, text
	




users = []
foods = []

# List for grouping meals
breakfast = [[0 for x in range(3)] for y in range(8)]
lunch = [[0 for x in range(3)] for y in range(8)]
dinner = [[0 for x in range(3)] for y in range(8)]

# Load database from file


#normal_user_view(user_name, age, gender, height, weight, weight_goal, activity_level);
