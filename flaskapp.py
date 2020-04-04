from flask import Flask
import requests, json
app = Flask(__name__)

@app.route("/user/", methods=["GET","POST"])
def get_userlist():
    ret=""
    try:
        if request.method == "GET":
            username = request.args.get('username')
            email = request.args.get('email')
            #SQL get all users
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
            username
            email
            id
            """
            ret =""+userId
        if request.method == "DELETE":
            #Nachfrage?
            #SQL delete user by "userId"
            ret = "200"
    return ret

if __name__ == "__main__":
    app.run(host='0.0.0.0')
