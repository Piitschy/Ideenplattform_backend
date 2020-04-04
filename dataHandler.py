import mysql.connector
sql = mysql.connector.connect(host='localhost',database='infoplattform',user='python',password='salami14')

class User:
    def __init__(self,id, email, firstname, lastname, username , advanced = False):
        self.id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.advanced = advanced



