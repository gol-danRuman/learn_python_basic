def add(self):
    # con = mysql.connector.connect(host='localhost', user='root')
    # cur = con.cursor()
    # return cur
    print('Called add')
    try:
        database_connection = 'mysql+mysqlconnector://root:mysql123@172.16.5.194:3306/test_db'
        print(database_connection)
        connection = mysql.connector.connect(host='localhost', user='root', database='Hello', password='mysql123')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ", db_Info)
        else:
            print("Error in Connection")
        print(connection)
        mycursor = connection.cursor()

        mycursor.execute("select database();")
        record = mycursor.fetchone()
        print("Your connected to - ", record)
        print(mycursor)
        mycursor.execute("CREATE TABLE access_token (token VARCHAR(255), value TEXT(255),email VARCHAR(255))")
        sql = "INSERT INTO access_token (token, value, email) VALUES (%s, %s,%s)"
        val = ("token", "jdkjfkldsf", "emailaddress")

        mycursor.execute(sql, val)
        connection.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)