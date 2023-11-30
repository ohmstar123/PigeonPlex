from flask import Flask, render_template, request, jsonify
import mysql.connector

#Contributors to backend - Aarya Patel and Ohm Patel

app = Flask()

# connect to the local database 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123@",
    database="PigeonPlex"
)

cursor = db.cursor()

# @app.route('/main')
# def index():
#     return render_template('index.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/admin')
# def admin():
#     return render_template('admin.html')

# @app.route('/account')
# def register():
#     return render_template('account.html')

# @app.route('/movie')
# def movie():
#     return render_template('movie.html')

# @app.route('/purchase')
# def purchase():
#     return render_template('purchase.html')

@app.route('/users', methods=['POST'])
def add_user():
    try:
        # retrieve user information from the front end
        data = request.get_json()

        # extract user details
        username = data.get('username')
        password = data.get('password')
        fname = data.get('firstName')
        lname = data.get('lastName')
        email = data.get('email')
        contact = data.get('contactNumber')
        cardNumber = data.get('cardNumber')
        cardExpiry = data.get('cardExpiry')
        cvv = data.get('cvv')

        # insert data into the database
        query = """INSERT INTO User 
        (username, password, firstName, lastName, email, contactNumber, cardNumber, cardExpiry, cvv) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """
        values = (username, password, fname, lname, email, contact, cardNumber, cardExpiry, cvv)
        cursor.execute(query, values)

        # commit changes
        db.commit()

        # return success message
        return jsonify({"message": "User created successfully"}, 200)
    except Exception as e:
        # handle errors
        return jsonify({"error": str(e)}, 500)

# @app.route('/users', methods=['GET'])
# def get_users():
#     try:
#         # query the database
#         query = """SELECT * FROM User;"""
#         cursor.execute(query)
        
#         # fetch all the results and return them
#         result = cursor.fetchall()
#         return jsonify(result, 200)

#     except Exception as e:
#         # return error message
#         return jsonify({'error': str(e)}, 500)

@app.route('/account', methods=['GET'])
def add_user():
    try:
        # retrieve user information from the front end
        data = request.get_json()
        username = data['username']
        password = data['password']

        # query the database for the user
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        # query the database for the admin
        cursor.execute("SELECT * FROM admins WHERE username = %s AND password = %s", (username, password))
        admin = cursor.fetchone()

        if admin:
            return jsonify({'role': 'admin'})
        elif user:
            return jsonify({'userID': user['id']})
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/users/getInfo/<int:id>', methods=['GET'])
def get_user(id):
    try:
        query = """SELECT * FROM User WHERE userID = %s;"""
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        return jsonify(result, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)},500)

# update user account by name
@app.route('/users/updateInfo/<str:username>', methods=['PUT'])
def update_user(username):
    try:
        # retrieve user information from the front end
        data = request.get_json()

        # extract user details
        password = data.get('password')
        contact = data.get('contactNumber')
        cardNumber = data.get('cardNumber')
        cardExpiry = data.get('cardExpiry')
        cvv = data.get('cvv')

        # update user query message
        query = """UPDATE User 
        SET password = %s, contact = %s, cardNumber = %s, cardExpiry = %s, cvv = %s
        WHERE username = %s;"""
        values = (password,contact, cardNumber, cardExpiry, cvv, username)
        cursor.execute(query, values)

        # commit changes
        db.commit()

        # return success message
        return jsonify({"message": "User updated successfully"}, 200)
    except Exception as e:
        # handle errors
        return jsonify({"error": str(e)}, 500)

# delete user account by username
@app.route('/admin/deleteUser/<str:username>', methods=['DELETE'])
def delete_user(username):
    try:
        # delete user query message
        query = "DELETE FROM User WHERE username = %s;"
        # execute query
        cursor.execute(query, (username,))
        # commit changes
        db.commit()
        # return success message
        return jsonify({'message': 'Succesfilly deleted user!'}, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)}, 500)


@app.route('/movies/addMovie', methods=['POST'])
def add_movie():
    try: 
        # retrieve inforamtion from the front end
        data = request.get_json()

        # extract movie details
        title = data.get('title')
        image = data.get('image')
        description = data.get('description')
        cast = data.get('cast')
        director = data.get('director')
        duration = data.get('duration')
        genre = data.get('genre')
        ratings = data.get('ratings')
        trailer = data.get('trailer')
            
        # insert data into the database
        query = """INSERT INTO Movie (title, image, description, cast, director, duration, genre, ratings, trailer) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (title, image, description, cast, director, duration, genre, ratings, trailer)
        cursor.execute(query, values)
        db.commit()
        return jsonify({"message": "Movie created successfully"}, 200)
    except Exception as e:
        # handle errors
        return jsonify({"error": str(e)}, 500)

# Define a new route that accepts a username as a parameter
@app.route('/login/check_username/<string:username>', methods=['GET'])
def check_username(username):
    try:
        # SQL query to check if the username exists in the User table
        query_user = "SELECT * FROM User WHERE username = %s"
        # SQL query to check if the username exists in the Admin table
        query_admin = "SELECT * FROM Admin WHERE username = %s"
        
        # Execute the first query
        cursor.execute(query_user, (username,))
        # Fetch the result
        result_user = cursor.fetchone()
        
        # Execute the second query
        cursor.execute(query_admin, (username,))
        # Fetch the result
        result_admin = cursor.fetchone()
        
        # If the username does not exist in both tables, return "username available"
        if result_user is None and result_admin is None:
            return jsonify({"message": "username available"}, 200)
        # If the username exists in either table, return "username not available"
        else:
            return jsonify({"message": "username not available"}, 200)
    # Handle any exceptions that occur during execution
    except Exception as e:
        return jsonify({"error": str(e)}, 500)

#With movieID and date from front end, add a schedule for that with 50 seats in morning, afternoon, evening. 
@app.route('/movies/addSchedule', methods=['POST'])
def add_schedule():
    try:
        # retrieve inforamtion from the front end
        data = request.get_json()

        # extract movie details
        movieID = data.get('movieID')
        date = data.get('date')
            
        # insert data into the database
        query = """INSERT INTO Schedule (movieID, date, morning, afternoon, evening)) 
        VALUES (%s, %s, 50, 50, 50)"""
        values = (movieID, date)
        cursor.execute(query, values)
        db.commit()
        return jsonify({"message": "Schedule created successfully"}, 200)
    except Exception as e:
        # handle errors
        return jsonify({"error": str(e)}, 500)

# get schedule by movie id
@app.route('/movies/schedule/<int:id>', methods=['GET'])
def get_schedule(id):
    try:
        query = """SELECT * FROM Schedule WHERE movieID = %s;"""
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        return jsonify(result, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)},500)

# with movieid and date, delete schedule
@app.route('/movies/deleteSchedule/<int:id>/<str:date>', methods=['DELETE'])
def delete_schedule(id, date):
    try:
        # delete schedule query message
        query = "DELETE FROM Schedule WHERE movieID = %s AND date = %s;"
        # execute query
        cursor.execute(query, (id, date,))
        # commit changes
        db.commit()
        # return success message
        return jsonify({'message': 'Succesfilly deleted schedule for movie!'}, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)}, 500)

# with movie title, get all amount of tickets sold
@app.route('/movies/ticketsSold/<str:title>', methods=['GET'])
def get_tickets_sold(title):
    try:
        query = """SELECT movie.title, SUM(Purchase.amount) AS total_sales FROM purchase INNER JOIN movie ON purchase.movieID = movie.movieID
        WHERE movie.title LIKE %s
        GROUP BY movie.title;"""
        cursor.execute(query, ('%'+title+'%',))
        result = cursor.fetchall()
        return jsonify(result, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)},500)

# with movie title, get all users who bought tickets
@app.route('/movies/users/<str:title>', methods=['GET'])
def get_users(title):
    try:
        query = """SELECT DISTINCT User.username FROM User INNER JOIN Purchase ON User.accountID = Purchase.accountID
        INNER JOIN Movie ON Purchase.movieID = Movie.movieID
        WHERE Movie.title LIKE %s;"""
        cursor.execute(query, ('%'+title+'%',))
        result = cursor.fetchall()
        return jsonify(result, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)},500)

# get random list of 50 movies
@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        # query the database
        query = """SELECT * FROM Movie WHERE movieID BETWEEN 1 AND 1000 ORDER BY RAND() LIMIT 50;"""
        cursor.execute(query)
        
        # fetch all the results and return them
        result = cursor.fetchall()
        return jsonify(result, 200)

    except Exception as e:
        # return error message
        return jsonify({'error': str(e)}, 500)

# delete all users who havent bought tickets in the last year
@app.route('/admin/deleteInactiveUsers', methods=['DELETE'])
def delete_inactive_users():
    try:
        # delete inactive users query message
        query = """DELETE FROM User WHERE accountID NOT IN ( SELECT DISTINCT accountID
        FROM Purchase WHERE date >= CURDATE() - INTERVAL 1 YEAR);"""
        # execute query
        cursor.execute(query)
        # commit changes
        db.commit()
        # return success message
        return jsonify({'message': 'Succesfilly deleted inactive users!'}, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)}, 500)

# get movie by title
@app.route('/movies/searchMovieName/<str:title>', methods=['GET'])
def get_movie(title):
    try:
        query = """SELECT movieID, title, image FROM Movie WHERE title LIKE %s LIMIT 45"""
        cursor.execute(query, (f'%{title}%',))
        result = cursor.fetchall()
        return jsonify(result, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)},500)

# get movie info and schedule by id
@app.route('/movies/info&Schedule/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    try:
        query = """SELECT DISTINCT Movie.*, Schedule.date, Schedule.morning, 
        Schedule.afternoon, Schedule.evening FROM Movie JOIN Schedule ON 
        Movie.movieID = Schedule.movieID WHERE Movie.movieID = %s"""        
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        return jsonify(result, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)},500)

# delete movie schedule
@app.route('/movies/deleteID/<int:id>', methods=['DELETE'])
def delete_movie_schedule(id):
    try:
        # delete movie schedule query message
        query = "DELETE FROM Schedule WHERE movieID = %s;"
        # execute query
        cursor.execute(query, (id,))
        # commit changes
        db.commit()
        # return success message
        return jsonify({'message': 'Succesfilly deleted schedule for movie!'}, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)}, 500)

# increase duration for horror movie by 2 minutes
@app.route('/movies/updateDuration', methods=['PUT'])
def update_duration():
    try:
        # update duration query message
        query = """UPDATE Movie SET duration = duration + 2 WHERE genre = 'Horror';"""
        # execute query
        cursor.execute(query)
        # commit changes
        db.commit()
        # return success message
        return jsonify({'message': 'Succesfilly updated duration for horror movies!'}, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)}, 500)

# decrease duration for horror movie by 2 minutes
@app.route('/movies/updateDuration', methods=['PUT'])
def update_duration():
    try:
        # update duration query message
        query = """UPDATE Movie SET duration = duration - 2 WHERE genre = 'Horror';"""
        # execute query
        cursor.execute(query)
        # commit changes
        db.commit()
        # return success message
        return jsonify({'message': 'Succesfilly updated duration for horror movies!'}, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)}, 500)

# get movie info by date
@app.route('/movies/getByDate/<str:date>', methods=['get'])
def get_movie_by_date(date):
    try:
        query = """SELECT Movie.movieID, Movie.title, Movie.image
                FROM Movie
                JOIN Schedule ON Movie.movieID = Schedule.movieID
                WHERE Schedule.date LIKE %s
                LIMIT 45;"""
        
        # execute query
        cursor.execute(query, (f'{date}%',)) #date = YYYY-MM-DD
        result = cursor.fetchall()
        return jsonify(result)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)}, 500)

# post purchase made by user id
@app.route('/purchases/<int:id>', methods=['POST'])
def add_purchase(id):
    try:
        # retrieve inforamtion from the front end
        data = request.get_json()

        # extract movie details
        accountID = data.get('accountID')
        movieID = data.get('movieID')
        date = data.get('date')
        MovieTime = data.get('movieTime')
        amount = data.get('amount')           
        # insert data into the database
        query = """INSERT INTO Purchase (accountID, movieID, date, MovieTime, amount)) 
        VALUES (%s, %s, %s, %s, %s)"""
        values = (accountID, movieID, date, MovieTime, amount)
        cursor.execute(query, values)
        db.commit()
        return jsonify({"message": "Purchase created successfully"}, 200)
    except Exception as e:
        # handle errors
        return jsonify({"error": str(e)}, 500)

# get all purchases made by user id
@app.route('/purchases/<int:id>', methods=['GET'])
def get_purchases(id):
    try:
        query = """SELECT * FROM Purchase WHERE userID = %s;"""
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        return jsonify(result, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)},500)
    
@app.route('/purchases/refund/<int:purchaseID>', methods=['PUT'])
def update_user(purchaseID):
    try:
        # update user query message
        query = """UPDATE Purchase
                SET date = CONCAT(CURDATE(), ', REFUND')
                WHERE purchaseID = %s;"""
        
        cursor.execute(query, purchaseID)
        # commit changes
        db.commit()
        # return success message
        return jsonify({"message": "Refund successful"}, 200)
    except Exception as e:
        # handle errors
        return jsonify({"error": str(e)}, 500)

# get all refunds made by user id
@app.route('/refunds/<int:id>', methods=['GET'])
def get_refunds(id):
    try:
        query = """CREATE VIEW RefundView AS
                SELECT *
                FROM Purchase
            WHERE date LIKE '%REFUND%';"""
        query = """SELECT * FROM Refund WHERE userID = %s;"""
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        return jsonify(result, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)},500)

# add schedule to movie
@app.route('/movies/schedule', methods=['POST'])
def add_schedule():
    try:
        # retrieve inforamtion from the front end
        data = request.get_json()

        # extract movie details
        movieID = data.get('movieID')
        date = data.get('date')
        time1 = data.get('time1')
        time2 = data.get('time2')
        time3 = data.get('time3')
            
        # insert data into the database
        query = """INSERT INTO Schedule (movieID, date, time1, time2, time3) 
        VALUES (%s, %s, %s, %s, %s)"""
        values = (movieID, date, time1, time2, time3)
        cursor.execute(query, values)
        db.commit()
        return jsonify({"message": "Schedule created successfully"}, 200)
    except Exception as e:
        # handle errors
        return jsonify({"error": str(e)}, 500)

# delete schedule by id and title
@app.route('/movies/schedule/<int:id>/<str:date>', methods=['DELETE'])
def delete_schedule(id, date):
    try:
        # delete schedule query message
        query = "DELETE FROM Schedule WHERE movieID = %s AND date = %s;"
        # execute query
        cursor.execute(query, (id, date,))
        # commit changes
        db.commit()
        # return success message
        return jsonify({'message': 'Succesfilly deleted schedule for movie!'}, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)}, 500)

# get movie schedule by movie id with 2 dates and 3 times
@app.route('/movies/schedule/<int:id>', methods=['GET'])
def get_movie_schedule(id):
    try:
        query = """SELECT * FROM Schedule WHERE movieID = %s;"""
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        return jsonify(result, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)},500)



if __name__ == '__main__':
    app.run(debug=True)

