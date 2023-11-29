from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask()

# connect to the local database 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123@",
    database="PigeonPlex"
)

cursor = db.cursor()

@app.route('/main')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/account')
def register():
    return render_template('account.html')

@app.route('/movie')
def movie():
    return render_template('movie.html')

@app.route('/purchase')
def purchase():
    return render_template('purchase.html')

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

@app.route('/users', methods=['GET'])
def get_users():
    try:
        # query the database
        query = """SELECT * FROM User;"""
        cursor.execute(query)
        
        # fetch all the results and return them
        result = cursor.fetchall()
        return jsonify(result, 200)

    except Exception as e:
        # return error message
        return jsonify({'error': str(e)}, 500)

@app.route('/users/<str:username>', methods=['GET'])
def get_user(username):
    try:
        query = """SELECT * FROM User WHERE username = %s;"""
        cursor.execute(query, (username,))
        result = cursor.fetchall()
        return jsonify(result, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)},500)

@app.route('/users/<str:username>', methods=['PUT'])
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
        SET password = %s, contactNumber = %s, cardNumber = %s, cardExpiry = %s, cvv = %s
        WHERE username = %s;"""
        values = (password, contact, cardNumber, cardExpiry, cvv, username)
        cursor.execute(query, values)

        # commit changes
        db.commit()

        # return success message
        return jsonify({"message": "User updated successfully"}, 200)
    except Exception as e:
        # handle errors
        return jsonify({"error": str(e)}, 500)

# delete user account by id
@app.route('/admin/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        # delete user query message
        query = "DELETE FROM User WHERE userID = %s;"
        # execute query
        cursor.execute(query, (id,))
        # commit changes
        db.commit()
        # return success message
        return jsonify({'message': 'Succesfilly deleted user!'}, 200)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)}, 500)


@app.route('/movies/add', methods=['POST'])
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

# get random list of 20 movies
@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        # query the database
        query = """SELECT * FROM Movie ORDER BY RAND() LIMIT 20;"""
        cursor.execute(query)
        
        # fetch all the results and return them
        result = cursor.fetchall()
        return jsonify(result, 200)

    except Exception as e:
        # return error message
        return jsonify({'error': str(e)}, 500)

# get movie by title
@app.route('/movies/<str:title>', methods=['GET'])
def get_movie(title):
    try:
        query = """SELECT * FROM Movie WHERE title = %s;"""
        cursor.execute(query, (title,))
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

@app.route('/movies/getByDate/<date>', methods=['get'])
def get_movie_by_date(date):
    try:
        query = """SELECT Movie.title, Movie.image, Movie.description, Movie.cast, Movie.director, Movie.duration, Movie.genre, Movie.ratings, Movie.trailer
                FROM Movie
                JOIN Schedule ON Movie.movieID = Schedule.movieID
                WHERE Schedule.date = '%s%';"""
        
        # execute query
        cursor.execute(query, (date,))
        result = cursor.fetchall()
        return jsonify(result)
    except Exception as e:
        # return error message
        return jsonify({'error': str(e)}, 500)


if __name__ == '__main__':
    app.run(debug=True)