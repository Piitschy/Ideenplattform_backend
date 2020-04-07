from flask import Flask, request
from dataHandler import *
import json, re
app = Flask(__name__)

regex={}#json.loads("conf/regex.json")

def object2json(obj,array=False):
    if obj is None:
        return json.dumps({"data":None,"code":204,"error":"Objekt nicht vorhanden"})
    if array:
        dataArray=[]
        for o in obj:
            obj_temp={}
            for attr, value in o.__dict__.items():
                obj_temp.update({attr:value})
            dataArray.append(obj_temp)
        data={"data":dataArray}
    else:
        obj_temp={}
        for attr, value in obj.__dict__.items():
            obj_temp.update({attr:value})
        data={"data":obj_temp}
    ret={}
    ret.update(data)
    ret.update({"code":200})
    return json.dumps(ret)

def validierung(eingabe,typ=None,regex=None):
    """
    Gleicht die Eingabe mit den in conf/ interlegten regular expressions ab
    """
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
    if request.method == "GET":
        """
        get a list of User-Object

        :param page: index of page
        :param size: size of page
        :param username: users username
        :param email: user email
        """
        page = validierung(request.args.get('page'),"int",regex)
        page = page if page is not None else 0
        size = validierung(request.args.get('size'),"int",regex)
        size = size if size is not None else 25
        username = validierung(request.args.get('username'),"uname",regex)
        email = validierung(request.args.get('email'),"email",regex)
        return object2json(loadUsers(page,size,email,username),array=True)

    if request.method == "POST":
        """
        create an User-Object

        :param id: the Id of the exist database entry or -1
        :param email: user email
        :param firstname: user firstname
        :param lastname: users lastname
        :param username: users username
        :param advanced: True if advanced permission active
        """
        r=request.get_json(force=True)
        print(r)
        #validierung
        u=User(id=-1,email=r["email"],firstname=r["firstname"],lastname=r["lastname"],username=r["username"])
        u.store(password= r["password"])

        return object2json(u)


@app.route("/user/<string:userId>", methods=["GET","DELETE"])
def parse_request(userId):
    ret=""
    if request.method == "GET":
        print(userId)
        return object2json(loadUser(int(userId)))
    if request.method == "DELETE":
        u=loadUser(userId)
        u.delete()
        return "200"

'''
#CONTENT
@app.route("/content/<string:contentId>", methods=["GET","DELETE"])
def parse_request(contentId):
    pass
    try:
        if request.method == "GET":
            """
            title=""
            tags=[(,),(,)]
            author=""
            comments=(,)
            sections = [Section]
            """
'''
if __name__ == "__main__":
    app.run(host='0.0.0.0')
