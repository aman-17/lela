from os import abort
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, send_file
from flask_login import login_required, current_user
from flask.globals import session
import json
#from app import app
from classes.User import User
# from . import getSuggestedMeal, normal_user_view

# from app import application, classes, db

# FLASK & WEB
from flask import flash, render_template, redirect, url_for, Response, request
from flask_login import current_user, login_user, login_required, logout_user

# UPLOADING & FILE PROCESSING
# from werkzeug import secure_filename
import os
import time
import ffmpy

# APP CODE
# import yoga_detection.process_openpose_user
# from yoga_detection.modeling import mean_ten_still_frames
# from yoga_detection.process_label import ProcessLabel


import time
import os
import math
from classes.User import User
from classes.Report import Report
from classes.Food import Food

views = Blueprint('views',__name__,template_folder="templates/",static_folder="../static/")# static_url_path="/static")

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

# @views.route('/static/<path:filename>', methods = ["GET","POST"])
# def serve_static(filename):
#     root_dir = os.path.dirname(os.getcwd())
#     print("Called Static File")
#     return send_file(os.path.join(root_dir, 'static'), filename)


@views.route('/h_gallery_animals', methods=['GET','POST'])
def h_gallery_animals():
    
    return render_template("h_gallery_animals.html", user=current_user)

@views.route('/h_gallery_diet', methods=['GET','POST'])
def h_gallery_diet():
    
    return render_template("h_gallery_diet.html", user=current_user)

@views.route('/h_gallery_environment', methods=['GET','POST'])
def h_gallery_environment():
    
    return render_template("h_gallery_environment.html", user=current_user)

@views.route('/h_gallery_fitness', methods=['GET','POST'])
def h_gallery_fitness():
    
    return render_template("h_gallery_fitness.html", user=current_user)

@views.route('/h_gallery_friends', methods=['GET','POST'])
def h_gallery_friends():
    
    return render_template("h_gallery_friends.html", user=current_user)

@views.route('/h_gallery_fruits', methods=['GET','POST'])
def h_gallery_fruits():
    
    return render_template("h_gallery_fruits.html", user=current_user)

@views.route('/h_gallery_gender', methods=['GET','POST'])
def h_gallery_gender():
    
    return render_template("h_gallery_gender.html", user=current_user)

@views.route('/h_gallery_heartbreak', methods=['GET','POST'])
def h_gallery_heartbreak():
    
    return render_template("h_gallery_heartbreak.html", user=current_user)

@views.route('/h_gallery_indoorsports', methods=['GET','POST'])
def h_gallery_indoorsports():
    
    return render_template("h_gallery_indoorsports.html", user=current_user)

@views.route('/h_gallery_keeptabs', methods=['GET','POST'])
def h_gallery_keeptabs():
    
    return render_template("h_gallery_keeptabs.html", user=current_user)

@views.route('/h_gallery_love', methods=['GET','POST'])
def h_gallery_love():
    
    return render_template("h_gallery_love.html", user=current_user)

@views.route('/h_gallery_music', methods=['GET','POST'])
def h_gallery_music():
    
    return render_template("h_gallery_music.html", user=current_user)

@views.route('/h_gallery_nature', methods=['GET','POST'])
def h_gallery_nature():
    
    return render_template("h_gallery_nature.html", user=current_user)

@views.route('/h_gallery_outdoorsports', methods=['GET','POST'])
def h_gallery_outdoorsports():
    
    return render_template("h_gallery_outdoorsports.html", user=current_user)

@views.route('/h_gallery_personalhealth', methods=['GET','POST'])
def h_gallery_personalhealth():
    
    return render_template("h_gallery_personalhealth.html", user=current_user)

@views.route('/h_gallery_pets', methods=['GET','POST'])
def h_gallery_pets():
    
    return render_template("h_gallery_pets.html", user=current_user)

@views.route('/h_gallery_pregnancy', methods=['GET','POST'])
def h_gallery_pregnancy():
    
    return render_template("h_gallery_pregnancy.html", user=current_user)

@views.route('/h_gallery_education', methods=['GET','POST'])
def h_gallery_education():
    
    return render_template("h_gallery_education.html", user=current_user)

@views.route('/h_gallery_technology', methods=['GET','POST'])
def h_gallery_technology():
    
    return render_template("h_gallery_technology.html", user=current_user)

@views.route('/h_gallery_travel', methods=['GET','POST'])
def h_gallery_travel():
    
    return render_template("h_gallery_travel.html", user=current_user)

@views.route('/h_gallery_water', methods=['GET','POST'])
def h_gallery_water():
    
    return render_template("h_gallery_water.html", user=current_user)

@views.route('/h_gallery_watersports', methods=['GET','POST'])
def h_gallery_watersports():
    
    return render_template("h_gallery_watersports.html", user=current_user)

@views.route('/h_gallery_work', methods=['GET','POST'])
def h_gallery_work():
    
    return render_template("h_gallery_work.html", user=current_user)

@views.route('/h_gallery_yoga', methods=['GET','POST'])
def h_gallery_yoga():
    
    return render_template("h_gallery_yoga.html", user=current_user)

@views.route('/poses', methods=['GET'])
def poses():
    return render_template('poses.html')

@views.route('/poses/<pose_id>', methods=['GET'])
def pose(pose_id):
    # select * from poses where id = pose_id
    pose_name = "Warrior II"
    pose_desc = "Good choice. Warrior II is a great pose to open your hips," \
        + " chest, and shoulders while strengthening your leg and abdomen."
    return render_template('pose.html',
                           pose_name=pose_name,
                           pose_desc=pose_desc)


@views.route('/video', methods=['POST'])
def video():
    if request.method == 'POST':
        file = request.files['file']

        filename = 'move'
		#filename = secure_filename(file.filename)
        print(type(file))
        file.save(os.path.join(views.config['UPLOAD_FOLDER'], filename))
        print(filename, views.config['UPLOAD_FOLDER'])
        timestr = time.strftime("%Y%m%d-%H%M%S")
        local_path = f"/tmp/user_video_{timestr}.avi"

        ff = ffmpy.FFmpeg(inputs={os.path.join(
                                  views.config['UPLOAD_FOLDER'],
                                  filename): None},
                          outputs={local_path: '-q:v 0 -vcodec mjpeg -r 30'})
        ff.run()
        timestr = time.strftime("%Y%m%d-%H%M%S")
        # filepath = push2s3(name, '') #filename without tmp

        # Process video with openpose on same server & return df
        df = process_openpose(local_path)
        # pull csv from s3, run through rules-based system
        labels, values = warrior2_label_csv(df)
        # user = load_user(uid)
        # user.labels = labels
        comma_separated = ','.join([str(int(c)) for c in labels])
        print(comma_separated)
        return url_for('feedback', labels_str=comma_separated)
    # return render_template('video.html')

# @application.route('/audio')
# def done_audio():
#     return send_file('done.m4a',
#                      mimetype="audio/m4a",
#                      as_atachment=True,
#                      attachment_filename='done.m4a')


@views.route('/feedback/<labels_str>', methods=['GET'])
@login_required
def feedback(labels_str):
    labels = list(labels_str.split(','))
    labels = [int(float(c)) for c in labels]
    pose_name = "Warrior II"
    # feedback = ProcessLabel.to_text([1, 1, 1, 1, 0, 0, 0, 0, 0])
    feedback_text = ProcessLabel.to_text(labels)
    return render_template('feedback.html',
                           feedback=feedback_text, pose_name=pose_name)



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




#modeling
import numpy as np
import pandas as pd
import math


def mean_ten_still_frames(pose_df):
    """
    This function find the ten stillest frames in the pose's df.
    It returns the mean for each point
    """
    # pose_df = pose_csv
    pose_diff = pose_df.diff()
    rows_total_diff = pose_diff.sum(axis=1)
    rows_total_diff = [abs(i) for i in rows_total_diff]
    ten_rows_diff = []
    for i in range(len(rows_total_diff)-10):
        ten_rows_diff.append((i, sum(rows_total_diff[i:(i+10)])))
    best_ten = sorted(ten_rows_diff, key=lambda x: x[1], reverse=False)
    still_point = best_ten[0][0]
    stillest_ten = pose_df.iloc[still_point:still_point+10, :]
    mean = np.mean(stillest_ten, axis=0)
    return mean


def x_y_points(data):
    """
    from array of average of points in a single 'pose_keypoints_2d' array
    finds x and y corridnates and return two lists
    """
    x_warrior = []
    y_warrior = []
    c_warrior = []  # certainity of pose
    for n in range(len(data)):
        if (n % 3) == 0:
            x_warrior.append(data[n])
        elif (n % 3) == 1:
            y_warrior.append(data[n])
        elif (n % 3) == 2:
            c_warrior.append(data[n])

    return x_warrior, y_warrior


def straight_arms_slope(x, y, min_slope=-0.10, max_slope=0.10, arm_slope=0.3):
    """
    input array of 25 x corridnates and array of 25 y corridinates
    from openpose (x_y_points(data))
    output is slope of the line from one hand to another
    perfectly straight arms would have a slope of zero.
    Checks that arms and shoulders are straight
    7:"LWrist" and 4:"RWrist"
    0 - straight
    1 - not straight
    returns slope and label
    """
    slope = (y[7]-y[4])/(x[7]-x[4])
    right_shoulder = (y[2]-y[4])/(x[2]-x[4])
    left_shoulder = (y[5]-y[4])/(x[5]-x[4])
    if min_slope <= slope <= max_slope \
        and abs(left_shoulder) <= arm_slope \
            and abs(right_shoulder) <= arm_slope:
            return slope, 0.0
    else:
        return slope, 1.0


def straight_arms_area(x, y, max_area=40, max_slope=0.07):
    """
    7:"LWrist"
    5: 'LShoulder'
    4:"RWrist"
    2: 'RShoulder'
    1: 'Neck'
    """
    d1 = (x[2]-x[5], y[2]-y[5])
    d2 = (x[4]-x[7], y[4]-y[7])
    A = .5 * abs((d1[0]*d1[1])-(d2[0]*d2[1]))
    arms_len = np.sqrt((x[7]-x[0])**2+(y[7]-y[0])**2)
    slope_shoulder = (y[5]-y[2])/(x[5]-x[2])

    if abs(A/arms_len) <= max_area and slope_shoulder <= max_slope:
        return (A/arms_len, slope_shoulder), 0.0
    else:
        return (A/arms_len, slope_shoulder), 1.0


def straight_arms(x, y, min_slope=-0.25, max_slope=0.25):
    slope_shoulder = (y[5]-y[2])/(x[5]-x[2])
    if min_slope <= slope_shoulder <= max_slope:
        return straight_arms_slope(x, y)
    else:
        return straight_arms_area(x, y)


def shoulders_up(x, y, max_angle=10):
    """
    1:"Neck",
    2:"RShoulder",
    5:"LShoulder".
    looks at line from left shoulder to neck, and
    line from right shoulder to neck
    if either are not straight returns 1
    if both are flat (slope of 0 or close to 0) returns 1
    """
    left_degrees = math.degrees(math.atan2(y[5]-y[1], x[5]-x[1]))
    right_degrees = math.degrees(math.atan2(y[1]-y[2], x[1]-x[2]))
    slope_shoulder = (y[5]-y[2])/(x[5]-x[2])
    if (left_degrees <= max_angle and
        right_degrees <= max_angle) \
            and slope_shoulder <= 0.25:
            return left_degrees, right_degrees, 0.0
    else:
        return left_degrees, right_degrees, 1.0


def hips_square(x, y, max_slope=0.1):
    """
    9:"RHip" and 12:"LHip"
    straight line (square hips) would have a slope of 0
    0 - stright
    1 - not straight
    """
    slope = (y[9] - y[12])/(x[9]-x[12])
    if -max_slope <= slope <= max_slope:
        return slope, 0.0
    else:
        return slope, 1.0


def straight_torso(x, y, min_slope=9):
    """
    1:"Neck" and 8:"MidHip"
    perfect would be a vertial line, so steep/high slope is ideal
    0 - straight
    1 - not straight
    returns slope and label
    """
    slope = (y[1] - y[8])/(x[1]-x[8])
    if abs(slope) >= min_slope:
        return slope, 0.0
    else:
        return slope, 1.0


def torso_forward(x, y, min_slope=-0.2):
    """
    1:"Neck" and 8:"MidHip"
    perfect would be a vertial line, so steep/high slope is ideal
    for too far forward we see if the slope if larger than the min slope
    0 - not too far forward
    1 - too far forward
    returns slope and label
    """
    rev_slope = (x[1]-x[8])/(y[1] - y[8])
    if rev_slope <= min_slope:
        return rev_slope, 1.0
    else:
        return rev_slope, 0.0


def torso_backward(x, y, min_slope=0.02):
    """
    1:"Neck" and 8:"MidHip"
    perfect would be a vertial line, so steep/high slope is ideal
    swtiches x and y for easier computation, want reversed
    slope to be zero if straight
    for too far forward we see if the slope if larger than the min slope
    0 - not too far forward
    1 - too far forward
    returns slope and label
    """
    rev_slope = (x[1]-x[8])/(y[1] - y[8])
    if rev_slope >= min_slope:
        return rev_slope, 1.0
    else:
        return rev_slope, 0.0


def head_front(x, y, max_ratio_diff=0.5, side='right'):
    """
    0:"Nose"
    15:"REye"
    16:"LEye"
    17:"REar"
    18:"LEar"
    Compares distance from left eye to right eye
    If looking forward eye to eye distance will be larger
    and closer to ear to ear distance
    If looking if head is front they will be small,
    and much smaller than ear to ear distance
    Divide by length from ear to ear to normalize and
    account for different distance
    label 0 - head is front
    label 1 - head is not facing the front (facing the side)
    """
    if side == 'right':
        ear_dist = np.sqrt((x[17]-x[0])**2+(y[17]-y[0])**2)
        eye_dist = np.sqrt((x[15]-x[0])**2+(y[15]-y[0])**2)
    else:
        ear_dist = np.sqrt((x[18]-x[0])**2+(y[18]-y[0])**2)
        eye_dist = np.sqrt((x[16]-x[0])**2+(y[16]-y[0])**2)
    ratio = eye_dist/ear_dist
    if ratio > max_ratio_diff:
        return ratio, 1.0
    else:
        return ratio, 0.0


def front_knee_obtuse(x, y, max_angle=75, side='right'):
    """
    10:"RKnee",
    11:"RAnkle",
    13:"LKnee",
    14:"LAnkle"
    """
    if side == 'right':
        degrees = math.degrees(math.atan2(y[14]-y[13], x[14]-x[13]))
    else:
        degrees = math.degrees(math.atan2(y[11]-y[10], x[11]-x[10]))
    if degrees < max_angle:
        return degrees, 1.0
    else:
        return degrees, 0.0


def front_knee_acute(x, y, min_angle=100, side='right'):
    """
    10:"RKnee",
    11:"RAnkle",
    13:"LKnee",
    14:"LAnkle"
    """
    if side == 'right':
        degrees = math.degrees(math.atan2(y[14]-y[13], x[14]-x[13]))
    else:
        degrees = math.degrees(math.atan2(y[11]-y[10], x[11]-x[10]))
    if degrees > min_angle:
        return degrees, 1.0
    else:
        return degrees, 0.0


def step_too_narrow(x, y, min_ratio=0.61):
    """
    4:"RWrist",
    7:"LWrist",
    11:"RAnkle",
    14:"LAnkle".
    compares arm span to distance between feet
    if feet are wide enough, the distance between feet will be similar
    to the distance between arms
    label - 0 feet are wide enough
    label - 1 feet are too narrow
    """
    arm_distance = np.sqrt((x[7]-x[4])**2+(y[7]-y[4])**2)
    feet_disatance = np.sqrt((x[11]-x[14])**2+(y[11]-y[14])**2)
    ratio = feet_disatance/arm_distance
    if ratio < min_ratio:
        return ratio, 1.0
    else:
        return ratio, 0.0


def step_too_wide(x, y, max_ratio=0.9):
    """
    4:"RWrist",
    7:"LWrist",
    11:"RAnkle",
    14:"LAnkle".
    compares arm span to distance between feet
    if feet are wide enough, the distance between feet will be similar
    to the distance between arms
    label - 0 feet are wide enough
    label - 1 feet are too narrow
    """
    arm_distance = np.sqrt((x[7]-x[4])**2+(y[7]-y[4])**2)
    feet_disatance = np.sqrt((x[11]-x[14])**2+(y[11]-y[14])**2)
    ratio = feet_disatance/arm_distance
    if ratio > max_ratio:
        return ratio, 1.0
    else:
        return ratio, 0.0


def warrior2_label_csv(pose_df, side='right'):
    """
    takes averages of all rows (2d_points)
    OLD order: head_front, sholders, arms, torso forward,
    torso backward hips, knee acute, knee obtuse, step wider
    1 - needs to be adjusted
    0 - good
    Order for 9 digit labeling:
    1. arms
    2. front_knee_obtuse
    3. front_knee_acute
    4. head_sideways
    5. hips_angled
    6. narrow_step
    7. shoulders_up
    8. torso_forward
    9. torso_backward
    10. wide_step
    """

    x, y = x_y_points(np.array(mean_ten_still_frames(pose_df)))
    # check whole body is in frame
    esstentials = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 21, 24]
    x_essentials = [x[i] for i in esstentials]
    y_essentials = [y[i] for i in esstentials]
    if (0.0 in y_essentials) or (0.0 in x_essentials):
        return [1.0 for i in range(10)], [1.0 for i in range(10)]
    labels = []
    values = []
    # 1 arms
    slope, label = straight_arms(x, y)
    labels.append(label)
    values.append(slope)
    # 2 and 3 front_knee_obtuse and front_knee_acute
    if side == 'right':
        obtuse_angle, obtuse_label = front_knee_obtuse(x, y, side='right')
        acute_angle, acute_label = front_knee_acute(x, y, side='right')
    else:
        obtuse_angle, obtuse_label = front_knee_obtuse(x, y, side='left')
        acute_angle, acute_label = front_knee_acute(x, y, side='left')
    labels.append(obtuse_label)
    values.append(obtuse_angle)
    labels.append(acute_label)
    values.append(acute_angle)
    # 4 head_sideways
    ratio, label = head_front(x, y)
    labels.append(label)
    values.append(ratio)
    # 5 hips_angled
    slope, label = hips_square(x, y)
    labels.append(label)
    values.append(slope)
    # 6 narrow_step
    ratio, label = step_too_narrow(x, y)
    labels.append(label)
    values.append(ratio)
    # 7 shoulders_up
    left_slope, right_slope, label = shoulders_up(x, y)
    labels.append(label)
    values.append((left_slope, right_slope))
    # 8 torso_forward
    slope, label = torso_forward(x, y)
    labels.append(label)
    values.append(slope)
    # 9 torso_backward
    slope, label = torso_backward(x, y)
    labels.append(label)
    values.append(slope)
    # 10 too wide step
    ratio, label = step_too_wide(x, y)
    labels.append(label)
    values.append(ratio)
    return labels, values


# process_label

import numpy as np
#  print("""
# 1. arms
# 2. front_knee_obtuse
# 3. front_knee_acute
# 4. head_sideways
# 5. hips_angled
# 6. narrow_step
# 7. shoulders_up
# 8. torso_forward
# 9. torso_backward
# 10. wide_step
# """)

# labels = [1, 1, 1, 1, 0, 0 ,0 , 0, 0]


class ProcessLabel:

    @classmethod
    def to_text(cls, labels: list):
        """Converts the labels from the model to English text feedback"""
        result = []

        trans_fd = {
            0: 'straighten your arms, keep palms facing down',
            1: 'make sure your front shin is perpendicular to the floor',
            2: 'make sure your knee is not extended beyond your ankle,but is \
                in line with the heel',
            3: 'turn your head and look over your front fingers. Fix your \
            gaze to increase the focus',
            4: 'square your hips and shoulders sideways towards the camera. \
               Engage your core! Tailbone down, belly in',
            5: 'make a wider step, your feet are too close together',
            6: 'drop your shoulders away from your ears and actively reach \
             towards both ends of the room',
            7: "stack your shoulders directly over your hips so that rib cage \
            isn't floating forward",
            8: "stack your shoulders directly over your hips so that rib cage \
                isn't floating backward",
            9: 'make a shorter stance, seems like your feet are be too wide \
            apart. Back leg straight and strong'
        }

        if labels.count(1) == 0:
            result.append('Excellent job! Keep it up, yogi! \
            Wanna try different pose?')

        if labels.count(1) == 1:
            index = np.where(np.array(labels) == 1)[0]
            output = trans_fd[index[0]]
            result.append(f'Very very nice! One little thing: \
            try to {output}!')

        if (labels.count(1) >= 2) and (labels.count(1) < 7):
            index = np.where(np.array(labels) == 1)[0]  # list
            result.append('Well done! Couple of things to keep \
            in mind for you:')
            ct = 0
            for i in index:
                result.append(f'\
                {trans_fd[i][0].capitalize() + trans_fd[i][1:]}.')
                ct += 1
                if ct == 3:
                    break

        if labels.count(1) >= 7:
            result.append("Are you sure you were following my instructions? \
            Let's try again!")

        return result

#process_openpose_user

import boto3
import os
import subprocess
import pandas as pd
import shutil
import json
from io import StringIO
from moviepy.editor import *


def df2csv_s3(df, s3_path, s3_path_avi, processed_path,
              bucket_name='alignedstorage'):
    """
    Convert Pandas dataframe to csv.
    Upload csv and processed avi to s3.
    Return dataframe.
    """
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    bucket.put_object(Key=s3_path, Body=csv_buffer.getvalue(),
                      ACL='public-read')
    # bucket.put_object(Key=s3_path_avi, Body=open(processed_path, 'rb'),
    #                  ACL='public-read')
    return df


def upload_and_delete(local_dir, s3_path, processed_path, s3_path_avi):
    """
    Convert pose keypoints from individual jsons to single df and
    upload to s3.
    Return dataframe of pose keypoints.
    """
    df = pd.DataFrame(columns=list(range(75)))
    for subdir, dirs, files in os.walk(local_dir):
        print(len(files))
        for i, file in enumerate(files):
            print(i)
            full_path = os.path.join(subdir, file)
            try:
                with open(full_path, 'r') as f:
                    json_file = json.load(f)
                data = json_file['people'][0]['pose_keypoints_2d']
                df.loc[i] = data
            # except UnicodeDecodeError:
            except:  # noqa: E722
                continue
        df = df2csv_s3(df=df, s3_path=s3_path, processed_path=processed_path,
                       s3_path_avi=s3_path_avi)
        shutil.rmtree(subdir)  # delete directory and contents
        return df


def process_openpose(path_local):
    '''
    Process local avi file using openpose software.
    Upload files to s3.
    Return dataframe of keypoints.
    '''
    dir, file_name = os.path.split(path_local)
    name, _ = os.path.splitext(file_name)
    path_s3_csv = 'output/' + name + '.csv'
    path_s3_avi = 'processed_videos/' + name + '_processed.avi'
    output_dir = "/tmp/json_data"  # without extension
    processed_path = "/tmp/" + name + "_processed.avi"
    # processed_path = "/home/ubuntu/product-analytics-group-project-group10
    # /code/aligned/app/static/videos/user_vid_processed.avi"
    openpose_path = \
        "/home/ubuntu/openpose/build/examples/openpose/openpose.bin"

    # Create output directory if necessary
    if os.path.isdir(output_dir) is False:
        os.mkdir(output_dir)

    # Run openpose on video
    openpose_cmd = [
        openpose_path,
        "--video",
        path_local,
        "--write_video",
        processed_path,
        "--write_json",
        output_dir,
        "--display",
        "0"]

    process = subprocess.Popen(openpose_cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr != '':
        print(stderr)

    # Create gif for feedback page
    # clip = VideoFileClip(processed_path).resize(0.3)
    # clip.write_gif("./app/static/videos/user_vid_processed.gif")

    mp4_path = '/home/ubuntu/product-analytics-group-project-group10/code/' \
               'aligned/app/static/videos/user_vid_processed.mp4'
    print('mp4 start')
    mp4_cmd = ['ffmpeg', '-y', '-i', processed_path, mp4_path]
    process = subprocess.Popen(mp4_cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr != '':
        print(stderr)
    print('mp4 done')
    # subprocess.call(f'ffmpeg -i {processed_path} {mp4_path}')
    # print('mp4 done')
    # Save output to s3 and delete locally
    df = upload_and_delete(local_dir=output_dir, processed_path=processed_path,
                           s3_path=path_s3_csv, s3_path_avi=path_s3_avi)
    os.remove(path_local)
    # os.remove(processed_path)
    return df