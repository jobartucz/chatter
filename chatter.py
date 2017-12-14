import pymysql.cursors # database
from threading import Thread # multithreading
import time
import datetime

# connect to the database
# The database "bartucz_chatter" is on mysql.s483.sureserver.com
# The user is chatterdbuser / ThisIsAReallyGoodPassword
connection = pymysql.connect(host='mysql.s483.sureserver.com',
                             user='chatterdbuser',
                             password='ThisIsAReallyGoodPassword',
                             db='bartucz_chatter',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select all Products
        sql = "SELECT * from chats"
        
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        for result in cursor:
            print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()


# If you want to be fancy, you'll need to set up a GUI to display messages
# this should probably be the last thing you do



# this function should get messages from the database and display them
def text_entry():
    newmessage = ""
    while (newmessage != "exit"):
        newmessage = input("> ")

        # this is where you'll have to insert the message into the database
    

# this function gets the messages from the database
def get_messages():
    # time_of_last_check = datetime from a long time ago to get all messages
    howlong = 10 # run for 10 seconds
    while (howlong > 0):
        # this is where you'll get the messages from the database since the last check and print them

        # set the time of last check to now, since we just checked them
        time_of_last_check = datetime.datetime
        
        # sleep for a little bit
        time.sleep(1)
        howlong -= 1


t1 = Thread(target=text_entry)
t2 = Thread(target=get_messages)
t1.start()
t2.start()


# if you "join" the threads to the main program, they will not die when the main program dies.
# The main program will wait for each thread to finish before exiting.
t1.join()
t2.join()

