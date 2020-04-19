import mysql.connector

def addToDB():
    # conection = mysql.connector.connect(host='172.16.5.194', user='user', passwd="pass", database='testing')
    conection = mysql.connector.connect(host='localhost', user='root', database='Hello')
    mycursor = conection.cursor()
    mycursor.execute("CREATE TABLE access_token (token VARCHAR(255), value TEXT(255),email VARCHAR(255))")
    sql = "INSERT INTO access_token (token, value, email) VALUES (%s, %s,%s)"
    val = ("token", "jdkjfkldsf", "emailaddress")

    mycursor.execute(sql, val)
    conection.commit()

def getFromDB(email):
    conection = mysql.connector.connect(host='localhost', user='root', database='Hello')
    mycursor = conection.cursor()
    sql = "SELECT * FROM access_token WHERE email ='%s'" %(email)

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
try:
    getFromDB('emailaddress')

except Exception as e:
    print('Error while saving acces token', e)