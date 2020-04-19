import mysql.connector

def showMySqlDB(con):
    mycursor = con.cursor()
    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
      print(x)

def createMySqlDB(con, database_name):
    mycursor = con.cursor()
    mycursor.execute("CREATE DATABASE %s" % (database_name))


def createMySqlDB_table(db_name,table_name):
    print(('hello create table'))
    con = mysql.connector.connect(host='localhost', user='root', database=db_name)
    mycursor = con.cursor()
    mycursor.execute("CREATE TABLE %s (token VARCHAR(255), value TEXT(255)" %(table_name))

def insertMySqlDb(db_name):
  try:
    print('hello insert')
    conection = mysql.connector.connect(host='localhost', user='root', database=db_name)
    mycursor = conection.cursor()
    sql = "INSERT INTO customer (token, value) VALUES (%s, %s)"
    val = ("token", "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik1URXhRVFE1TVVRNE9EQkJRMFpGTjBSRE5EVkdSRGRGUWpBMk0wRXdNalkyT1RNNU9VVXdOUSJ9.eyJpc3MiOiJodHRwczovL2FiY2RlZi0xMjMuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEwMjkxOTQ1MzMyMzU2NzU5ODk4IiwiYXVkIjpbIkhyLWJhY2tlbmQiLCJodHRwczovL2FiY2RlZi0xMjMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU1ODYwMjQwMCwiZXhwIjoxNTU4Njg4ODAwLCJhenAiOiJpalkwaXMzSjlPclkweU1QeDFaVkxLYVJDOGVZemxQRiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwifQ.W78eKZN-RfKk7N1fD5fQBh36ufUuIxi0z5QY5p8syB5Wsp-lH_EC59az8fHolXOiAwM1VYjrf7D0s2ry3RjA2lwiEIqK0X060xFaPzgOmdzY4m3BYbJ2cPXvduVTMwSFd--fU13ohuY9O4H7toC_qKPXoo6GffvcZwNV86dxcGcAapULAzx7O-glHWN9C-u7phjmrHaWK7ryhMgFjpEQdhQ2ZfN1rzZdsxUYXnWDIXiGB-gINQ5BpoW7YhniCN8JzzENUQenKELs-PpArYNs0LVZWdOw-QQ6ZFHW9QnSd1lSAwVkgOEdykTRapB47h6NYMR4cWfqVJiRx7wCD3JBUQ")
    mycursor.execute(sql, val)
    conection.commit()

    print(mycursor.rowcount, "record inserted.")

  except Exception as e:
    print('Error', e)

if __name__=='__main__':
  try:
    con = mysql.connector.connect(host='localhost',user= 'root')
    cur = con.cursor()

    # showMySqlDB(con)

    db_name = 'Hello'
    # createMySqlDB(con, db_name)
    # table_name = 'customer'
    # createMySqlDB_table(db_name, table_name)

    # val = ('ruman', 'lalitpur')
    insertMySqlDb(db_name)



  except mysql.connector.Error as e:

    print
    "Error %d: %s" % (e.args[0], e.args[1])


  finally:

    if con:
      con.close()

