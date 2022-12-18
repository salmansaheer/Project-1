from flask import render_template, make_response,request
from flask.blueprints import Blueprint
import os

home = Blueprint('HOME',__name__)

@home.route('/',methods = ['GET'])
def my_home():
    return render_template('/user/home_.html')
    