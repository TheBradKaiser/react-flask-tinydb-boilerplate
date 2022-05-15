from flask import Flask, request, Response
from database import db, usertable, uniqueInsert, votetable, countVotes, where
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

#POLL VOTE
@api.route('/voteForm', methods=['POST'])
def voteForm():
    votetable.insert(request.form)
    return "vote cast successfully"

#POLL RESULTS
@api.route('/voteGet')
def voteGet():
    votes = countVotes(votetable)
    response_body = votes
    return response_body


@api.route('/createPoll', methods=['POST'])
def createPoll():
    print(request.form)
    table = db.table(request.form['table'])
    return "table created successfully."

@api.route('/votePoll/<table>/', methods=['POST'])
def votePoll(table):
    optionsTable = db.table(table+"-options")
    print(request.form)
    if (optionsTable.search(where('test') == request.form['test']) != []):
        voteTable = db.table(table)
        voteTable.insert(request.form)
        return "vote cast successfully."
    else:
        return "option not valid"

@api.route('/getPollResults/<table>/')
def getPollResults(table):
    voteTable = db.table(table)
    votes = countVotes(voteTable)
    response_body = votes
    return response_body


@api.route('/addOption/<table>', methods=['POST'])
def addOption(table):
    optionsTable = db.table(str(table)+"-options")
    response_body= uniqueInsert(optionsTable,request.form)
    return str(response_body)

