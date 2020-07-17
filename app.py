from flask import Flask, request, render_template, redirect, url_for
import os
from dotenv import load_dotenv
import init_db
import sqlite3
load_dotenv()
# from datetime import datetime

app = Flask(__name__)

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

loggedIn = False
teamSizeLimit = 4

if (loggedIn == True):
    @app.route('/ctf', methods=['POST'])
    def flags():
        flag = request.form["flag"]
        processed_text = flag.upper()
        first_flag = os.getenv("FLAG_1")
        print(first_flag)
        if (processed_text == first_flag):
            correct_answer = "Your flag is correct!"
        else:
            correct_answer = "Your flag is incorrect. Please try again."
        return render_template("index.html", is_correct = correct_answer, flag=flag)
else:
    @app.route('/', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            if request.form['userteam'] :
                error = 'Team is full, please try another team.'
            else:
                loggedIn = True
                username = request.form['username']
                userteam = request.form['userteam']

                cursor.execute("INSERT INTO Users ")
                return render_template('index.html')
        return render_template('login.html', error=error)





 # Launch the FlaskPy dev server
app.run(host="localhost", debug=True)

# def hello():
#     if 'name' in request.args:
#         name = request.args['name']
#     else:
#         name = 'World'
#     return """
#          <html><body>
#              <h1>Hello, {0}!</h1>
#              The time is {1}.
#          </body></html>
#          """.format(
#              name, str(datetime.now()))