import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='av6352tk',
                             password='Buddha414!',
                             db='av6352tk_University',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select all Students
        key = input("Enter a name to search:\n" )
        sql = "SELECT * from Students WHERE Name LIKE %s"
        #sql = "SELECT * from Students WHERE Name = '" + key + "'"
        #sql = "SELECT * from Students WHERE Name = '" + key + "'"
        
        # execute the SQL command
        cursor.execute(sql, (key,))
        #cursor.execute(sql)

        # get the results
        for result in cursor:
            print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()

