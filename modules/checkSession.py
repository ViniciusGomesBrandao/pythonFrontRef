from flask import Flask, request, render_template, redirect, session
from flask_session import Session

def checkSessionToken():
    if(session.get('token')):
        return True
    elif(session.get('token') == ''):   
        return False
    else:
        return False