import mysql.connector
sql = mysql.connector.connect(host='localhost',database='infoplattform',user='python',password='salami14')

sessions = {}
def loadSession(SessionId):
    if SessionId in sessions:
        return sessions[SessionId]
    else:
        return -1



def loadUser(id):
    pass

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

    def delete(self):
        """
        delete Entry in database with given id
        :return:
        """
        cursor = sql.getCursor()
        cursor.execute(self.deleteQuery, (self.id,))
        sql.commit()
    def store(self , password):
        """
        stores the dataset to database
        if id not -1 try to update

        :param password: userpassword only change if value is set can't be none if id is -1
        :return: was successful
        """
        if self.id == -1 and None == password:
            return False
        cursor = sql.getCursor()
        if self.id == -1:
            cursor.execute(self.insertQuery,(self.email,self.firstname,self.lastname,self.username, password))

        elif password:
            cursor.execute(self.updatePasswordQuery,(self.email,self.firstname,self.lastname,self.username, password,self.id))
        else:
            cursor.execute(self.updateQuery,(self.email,self.firstname,self.lastname,self.username ,self.id))
        sql.commit()
        if cursor.rowcount == 0:
            return False
        self.id = cursor.lastrowid