from os import error
from flask import Flask, request, render_template, redirect, session
from flask_session import Session
from flask.templating import render_template_string
from werkzeug.utils import escape 
import os
from werkzeug.wrappers import response
from enviroment.enviroment import ENVIROMENT
from controllers.index  import indexController
from controllers.login import loginController
from controllers.home import homeController

template_dir = os.path.abspath('./')
app = Flask(__name__,  template_folder=template_dir)
app.register_blueprint(indexController)
app.register_blueprint(loginController)
app.register_blueprint(homeController)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('./templates/notFound/notFound.html'), 404
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
if __name__ == '__main__':
  app.run(debug=True)
