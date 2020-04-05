import json

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

class User:
    """
    Object represent a User
    """
    insertQuery = "INSERT INTO User (email, firstname, lastname, username, password) VALUES (%s,%s,%s,%s,SHA1(%s))"
    updateQuery = "UPDATE User SET email = %s, firstname = %s, lastname = %s, username = %s WHERE id = %s)"
    deleteQuery = "DELETE FROM User WHERE id = %s)"
    updatePasswordQuery = "UPDATE User SET email = %s, firstname = %s, lastname = %s, username = %s ,password = %s WHERE id = %s)"

    def __init__(self,id, email, firstname, lastname, username, advanced = False):
        """

        :param id: the Id of the exist database entry or -1
        :param email: user email
        :param firstname: user firstname only loaded if advanced Permission active
        :param lastname: users lastname only loaded if advanced Permissions active
        :param username: users username
        :param advanced: True if advanced permission active
        """
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.advanced = advanced

u=User("1234","dnsklf","Jan","Pietsch","Piitschy")
liste=[u,u]
print(object2json(u))
print(object2json(liste,array=True))