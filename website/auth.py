from os import abort
import os, pathlib
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.globals import session

from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
import requests
from pip._vendor import cachecontrol

from google_auth_oauthlib.flow import Flow
import google.auth.transport.requests
from google.oauth2 import id_token



from flask_login import login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


GOOGLE_CLIENT_ID = "948625510797-cgmbnruvkojgufaq24cfnd2vk14d2e09.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback/"
)

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)
            #return None
        else:
            return function()
    return wrapper


auth = Blueprint('auth', __name__)

@auth.route('/callback')
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/index")

@auth.route('/login')
def login():

    return render_template("login.html")

@auth.route('/login_auth')
def login_auth():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@auth.route('/logout')
@login_is_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('auth.login'))



