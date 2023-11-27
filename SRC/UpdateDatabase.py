# Use Python Verison 3.9
import mysql.connector, csv, random
from datetime import datetime, timedelta

def connect_database():
    return mysql.connector.connect(
        host='localhost',
        database='PigeonPlex',
        user='root',
        password='password1234'
    )

def insertMovie(title, image, description, cast, director, duration, genre, ratings, trailer):
    connection = connect_database()
    cursor = connection.cursor()
    mySqlInsertQuery = """INSERT INTO Movie (title, image, description, cast, director, duration, genre, ratings, trailer) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """
    movie = (title, image, description, cast, director, duration, genre, ratings, trailer)
    cursor.execute(mySqlInsertQuery, movie)
    connection.commit()
    cursor.close()
    connection.close()

def insertUser(username, password, firstName, lastName, email, contactNumber, cardNumber, cardExpiry, cvv):
    connection = connect_database()
    cursor = connection.cursor()
    mySqlInsertQuery = """INSERT INTO User (username, password, firstName, lastName, email, contactNumber, cardNumber, cardExpiry, cvv) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """
    user = (username, password, firstName, lastName, email, contactNumber, cardNumber, cardExpiry, cvv)
    cursor.execute(mySqlInsertQuery, user)
    connection.commit()
    cursor.close()
    connection.close()

def getMovieID(limit=1000):
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("SELECT movieID FROM Movie LIMIT %s", (limit,))
    movie_ids = [row[0] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    return movie_ids

def insertSchedule(movie_id, date, morning, afternoon, evening):
    connection = connect_database()
    cursor = connection.cursor()
    insert_query = """INSERT INTO Schedule (movieID, date, morning, afternoon, evening) 
                      VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(insert_query, (movie_id, date, morning, afternoon, evening))
    connection.commit()
    cursor.close()
    connection.close()

def addAdmin(adminUsers):
    connection = connect_database()
    cursor = connection.cursor()

    insert_query = """INSERT INTO Admin (username, password, firstName, lastName, email) 
                      VALUES (%s, %s, %s, %s, %s) """

    for user in adminUsers:
        cursor.execute(insert_query, user)
        print(user[0] + " As Admin Have Been Added")
    
    connection.commit()
    cursor.close()
    connection.close()

def uploadCSV():
    # Insert Movie Data
    with open('Data_Files/Movies_List.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        movieCount = 0
        for line_count, row in enumerate(csv_reader):
            if line_count > 0:
                cast = f'{row[7]}, {row[8]}, {row[9]}, {row[10]}'
                trailer = 'https://www.youtube.com/'
                ratings = row[5] if row[5] else -1
                insertMovie(row[1], row[0], row[4], cast, row[6], row[2], row[3], ratings, trailer)
                movieCount += 1
                print(str(movieCount) + " Movie(s) Added")

    # Insert User Data
    with open('Data_Files/User_Information.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        userCount = 0
        for line_count, row in enumerate(csv_reader):
            if line_count > 0:
                insertUser(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                userCount += 1
                print(str(userCount) + " User(s) Added")

def updatePurchase(accountID, movieID, date, movieTime, amount):
    connection = connect_database()
    cursor = connection.cursor()

    mySqlInsertQuery = """INSERT INTO purchase (accountID, movieID, date, movieTime, amount) 
                                VALUES (%s, %s, %s, %s, %s) """

    user = (accountID, movieID, date, movieTime, amount)
    cursor.execute(mySqlInsertQuery, user)
   
    

    connection.commit()
    cursor.close()
    connection.close()
    
def updateSchedule():
    scheduleUpdate = 0
    for i in range(1,1001):
        start_date = datetime.now()
        date1 = start_date + timedelta(days = i)
        date2 = start_date + timedelta(days = (i + 1))
        insertSchedule(i, date1, 50, 50, 50)
        insertSchedule(i, date2, 50, 50, 50)
        scheduleUpdate += 1
        print(str(scheduleUpdate) + " Movie Schedule Updated")

# Main execution
if __name__ == "__main__":
    uploadCSV()
    updateSchedule()

    admin = [
    ("James", "james1234", "James", "Jones", "jamesjones@gmail.com"),
    ("Alex", "alex1234", "Alex", "Camps", "alexcamps@gmail.com"),
    ("Brad", "brad1234", "Brad", "Pitt", "bradpitt@yahoo.com")
    ]

    addAdmin(admin)

    purchaseCounter = 0

    for i in range(1, 1001):
        movieID = random.randint(1, 1000)
        
        start_date = datetime.now()
        date = start_date + timedelta(days = i)
        
        accountID = random.randint(1, 560)
        time = random.randint(1, 3)
        
        movieTime = None
        if (time == 1):
            movieTime = 'morning'
        elif (time == 2):
            movieTime = 'afternoon'
        else:
            movieTime = 'evening'
        amount = round(random.uniform(15, 30), 2)
        
        updatePurchase(accountID, movieID, date, movieTime, amount)
        
        purchaseCounter += 1
        print(str(purchaseCounter) + " Purchases Completed")

    print("Database Setup Complete")