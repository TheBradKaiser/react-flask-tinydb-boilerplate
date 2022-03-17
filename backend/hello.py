from flask import Flask, request, Response
from database import db, usertable, uniqueInsert
import tinydb as tdb


api = Flask(__name__)

#normal get
@api.route('/home/<id>')
def my_profile(id):
    user = usertable.get(doc_id=id)
    response_body = {
        "username": user['username'],
        "password" :user['password']
    }

    return response_body


#get password for user of username
@api.route('/user/<username>')
def profile(username):

    user = usertable.search(tdb.where('username')==username)
    return user[0]['password']


#form post and insert into db example
@api.route('/form', methods=['POST'])
def form():

    response = uniqueInsert(usertable,request.form)
    return response


#either or
@api.route('/logins', methods=['GET', 'POST'])
def logins():
    if request.method == 'POST':
        return "posted "+str(request.form)
    else:
        return "got"