from os import abort
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, send_file
from flask_login import login_required, current_user
from flask.globals import session
from .models import Note
from . import db
import json
from website import create_app
from classes.User import User
from main import getSuggestedMeal, normal_user_view
from .auth import login_is_required


views = Blueprint('views', __name__)


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

@views.route('/h_about', methods=['GET','POST'])
def h_about():
   
    return render_template("h_about.html", user=current_user)

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