import mysql.connector
sql = mysql.connector.connect(host='localhost',database='infoplattform',user='python',password='salami14')
mycursor = sql.cursor()
mycursor.execute("SELECT text FROM test")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
