from flask import Blueprint, make_response,request

home = Blueprint('home',__name__)

@home.route('/',methods = ['GET'])
def my_home():
    pass