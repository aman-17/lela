from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, send_file
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from website import create_app
from classes.User import User
from Main import getSuggestedMeal, normal_user_view



views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    
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

@views.route('/about', methods=['GET','POST'])
@login_required
def about():
   
    
    return render_template("about.html", user=current_user)
   

@views.route('/recipe', methods=['GET','POST'])
@login_required
def recipe():
   
    
    return render_template("recipe.html", user=current_user)


@views.route('/logoutbutton', methods=['GET','POST'])
@login_required
def logoutbutton():
   
    
    return render_template("logoutbutton.html", user=current_user)

@views.route('/index', methods=['GET','POST'])
@login_required
def index():
   
    
    return render_template("index.html", user=current_user)

@views.route('/reportdownload', methods=['GET','POST'])
@login_required
def reportdownload():
   
    
    return send_file('/home/aman17/Flask-Web-App/user_reports/Aman_diet_report.txt')