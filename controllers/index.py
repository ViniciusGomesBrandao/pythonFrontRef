from modules.checkSession import *
from flask import Blueprint, redirect
indexController = Blueprint('indexController',__name__)
@indexController.route("/")
def main():
    if(checkSessionToken()):
        return redirect('home')
    else:
        return redirect('login')