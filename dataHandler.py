import mysql.connector
sql = mysql.connector.connect(host='localhost',database='infoplattform',user='python',password='salami14')

def loadUser:
    pass

class User:
    """
    Object represent a User
    """
    insertQuery = "INSERT INTO User (email, firstname, lastname, username, password) VALUES (%s,%s,%s,%s,SHA1(%s))"
    updateQuery = "INSERT INTO User (email, firstname, lastname, username, password) VALUES (%s,%s,%s,%s,SHA1(%s))"
    insertQuery = "INSERT INTO User (email, firstname, lastname, username, password) VALUES (%s,%s,%s,%s,SHA1(%s))"

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

    def store(self , password):
        """
        stores the dataset to database
        if id not -1 try to update

        :param password: userpassword only change if value is set can't be none if id is -1
        :return: was successful
        """
        if self.id == -1 and None == password:
            return False




