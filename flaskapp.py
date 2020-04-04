from flask import Flask, request
from dataHandler import *
import json, re
app = Flask(__name__)

def object2json(object):
    ret={}
    for attr, value in object.__dict__.items():
        ret.update({attr:value})
    return json.dumps(ret)

def validierung(eingabe,typ=None,regex=None):
    return eingabe
    """
    if isinstance(eingabe, str) or typ==None:
        return False
    for reg in regex:
        if re.search(regex[reg],eingabe):
            return eingabe
    return False
    """

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
            email = validierung(request.form('email'),"email",regex)
            firstname = validierung(request.form('firstname'),"name",regex)
            lastname = validierung(request.form('lastname'),"name",regex)
            username = validierung(request.form('username'),"uname",regex)
            paras = (email,firstname,lastname,username)
            if None in paras:
                ret="202 Bad Data"
            u=User(-1,email,firstname,lastname,username)
            u.store(None)
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
            return object2json(loadUser(userId))
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
    regex={}#json.loads("conf/regex.json")
    app.run(host='0.0.0.0')
