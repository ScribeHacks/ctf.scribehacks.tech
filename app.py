from flask import Flask, request, render_template, redirect, url_for, Blueprint
import os
from dotenv import load_dotenv
import sqlite3

# from datetime import datetime

app = Flask(__name__)
load_dotenv()

connection = sqlite3.connect('database.db')
db = SQLAlchemy()


loggedIn = False
teamSizeLimit = 4
currentID = 0
username = ""
userteam = ""


@main.route('/')
def index():
    return render_template('index.html')


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

# flag = request.form["flag"]
# processed_text = flag.upper()
# first_flag = os.getenv("FLAG_1")
# print(first_flag)
# if processed_text == first_flag:
#     correct_answer = "Your flag is correct!"
# else:
#     correct_answer = "Your flag is incorrect. Please try again."
# return render_template("index.html", is_correct=correct_answer, flag=flag)

# if loggedIn == True:


# @app.route('/ctf', methods=['GET', 'POST'])
# def flags():
#     global loggedIn
#     while loggedIn == True:
#         global username
#         global userteam
#         # global loggedIn
#         if request.form['btn_logout'] == 'logout':
#             # global loggedIn
#             loggedIn = False
#         return render_template("index.html", username=username, userteam=userteam)
#     else:
#         return redirect('/')
# @app.route('/', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] == '' or request.form['userteam'] == '':
#             error = 'Did not provide either username or team'
#         else:
#             global currentID
#             currentID += 1
#             global username
#             global userteam
#             username = request.form['username']
#             userteam = request.form['userteam']
#             with sqlite3.connect('database.db') as con:
#                 cursor = con.cursor()
#                 if cursor.execute("SELECT UserCount FROM Teams WHERE TeamName = ?", (userteam,)) == 4:
#                     error = "Team is full"
#                 else:
#                     cursor.execute(
#                         "UPDATE Teams SET UserCount = UserCount + 1 WHERE TeamName = ?", (userteam,))
#                     cursor.execute(
#                         "INSERT INTO Users (Username, Team) VALUES (?, ?)", (username, userteam))
#                     error = ''
#                 con.commit()
#             global loggedIn
#             if error == '':
#                 loggedIn = True
#                 return redirect('/ctf')
#     return render_template('login.html', error=error)
