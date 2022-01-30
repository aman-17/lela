from logging import debug
from website.views import views
from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'aman17'
    return app

app = create_app()

app.register_blueprint(views)

if __name__ == '__main__':
    # app.run(host="0.0.0.0",port=os.environ.get("PORT",5000))
    app.run(debug=True)


