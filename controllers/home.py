from modules.checkSession import *
from flask import Flask, request, render_template, redirect, session, Blueprint
import requests
from enviroment.enviroment import ENVIROMENT
homeController = Blueprint('homeController',__name__)
@homeController.route("/home")
def homePage():
    
        
    if(checkSessionToken()):
        return render_template('./templates/home/home.html', token=session.get('token'))
    else:
        return redirect("login")

@homeController.route('/home/getCollections', methods=["POST", "GET"])
def getCollections():
    if(request.method == "POST"):
        responseRequest = requests.get(f"{ENVIROMENT['API']}/collection/get", headers={
            "Authorization": f"Bearer {session.get('token')}"
        }).text
        return responseRequest
    else:
        return render_template('./templates/notFound/notFound.html')