import mysql.connector
sql = mysql.connector.connect(host='localhost',database='infoplattform',user='python',password='salami14')
mycursor = sql.cursor()
mycursor.execute("SELECT text FROM test")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

class User:
    def __init__(self, firstname, lastname, username):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        


