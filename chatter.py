import pymysql.cursors # database
from threading import Thread, Event # multithreading
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
def text_entry(arg1, stop_event):
    newmessage = ""
    while (newmessage != "exit"):
        newmessage = input("> ")

        # this is where you'll have to insert the message into the database
    stop_event.set()

# this function gets the messages from the database
def get_messages(arg1, stop_event):
    time_of_last_check = datetime.datetime(1975, 4, 3, 1, 1) # set the last time check to a long time ago
    # print(time_of_last_check.strftime("%A, %d. %B %Y %I:%M%p"))
    
    while (not stop_event.is_set()):
        # this is where you'll get the messages from the database since the last check and print them

        # set the time of last check to now, since we just checked them
        time_of_last_check = datetime.datetime.today()
        # print(time_of_last_check.strftime("%A, %d. %B %Y %I:%M%p"))
        
        # sleep for a little bit
        time.sleep(1)

# this is the threading "event" we'll use to stop reading the database when the user types "exit"
t2_stop = Event()

# start the threads
t1 = Thread(target=text_entry, args=(1, t2_stop))
t2 = Thread(target=get_messages, args=(2, t2_stop))
t1.start()
t2.start()


# if you "join" the threads to the main program, they will not die when the main program dies.
# The main program will wait for each thread to finish before exiting.
t1.join()
t2.join()
