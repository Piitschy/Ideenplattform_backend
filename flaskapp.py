from flask import Flask, request
from dataHandler import *
import json
app = Flask(__name__)

def null(x):
    if x == None:
        return ""
    else:
        return x


#USER
@app.route("/user", methods=["GET","POST"])
def get_userlist():
    ret=""
    try:
        if request.method == "GET":
            username = null(request.args.get('username'))
            email = null(request.args.get('email'))
            #SQL get all users
            ret="200"

        if request.method == "POST":
            username = null(request.form('username'))
            email = null(request.form('email'))
            firstname = null(request.form('firstname'))
            lastname = null(request.form('lastname'))
            #SQL write dates
            ret="200"
    except:
        ret="202"
    return ret

@app.route("/user/<string:userId>", methods=["GET","DELETE"])
def parse_request(userId):
    ret=""
    try:
        if request.method == "GET":
            #SQL get user by "userId"
            """
            username=""
            email=""
            firstname=""
            lastname=""
            """
            ret =json.dumps()
        if request.method == "DELETE":
            #Nachfrage?
            #SQL delete user by "userId"
            ret = "200"
    except:
        ret="202"
    return ret

#CONTENT
@app.route("/content/<string:contentId>", methods=["GET","DELETE"])
def parse_request(contentId):
    ret=""
    try:
        if request.method == "GET":
            """
            title=""
            tags=[(,),(,)]
            author=""
            comments=(,)
            sections = [Section]
            """
            


if __name__ == "__main__":
    app.run(host='0.0.0.0')
