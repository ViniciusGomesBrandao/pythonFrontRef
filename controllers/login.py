from modules.checkSession import *
from flask import Blueprint, render_template, session, abort, redirect
import json
import requests
from enviroment.enviroment import ENVIROMENT
loginController = Blueprint('loginController',__name__)
@loginController.route("/login", methods=["GET", "POST"])
def loginPage():
    if(request.method == "GET"):
        session['token'] = ''
        return render_template('./templates/login.html', errorInput=False)
    else: 
        user = request.form.get("user")
        password = request.form.get('password')
        if(user and password):
            response = json.loads( requests.post(f"{ENVIROMENT['API']}/auth/login", data={
                "user": user,
                "password": password
            }).text)
            try:
                session['token'] = response['token']
                return redirect("/home", code=302)
            except:
                return response
        else:
            return render_template('./templates/login.html', errorInput=False)