from flask import Flask, request, render_template, redirect, url_for, Blueprint
import os
from dotenv import load_dotenv
import sqlite3

app = Flask(__name__)
load_dotenv()

connection = sqlite3.connect('database.db')

teamSizeLimit = 4
currentID = 0
userteam = ""
error = None
username = ""
loggedIn = True


@app.route('/ctf', methods=['GET', 'POST'])
def ctf():
    if loggedIn == True:
        return render_template('ctf.html')
    if loggedIn == False:
        return redirect('/')


@app.route('/', methods=['GET', 'POST'])
def login():
    global loggedIn
    if loggedIn == False:
        global error
        global currentID
        global userteam
        if request.method == 'POST':
            if request.form['userteam'] == '':
                print('Did not provide a team')
            else:
                currentID += 1
                userteam = request.form['userteam']
                with sqlite3.connect('database.db') as con:
                    cursor = con.cursor()
                    cursor.execute(
                        "INSERT INTO Teams (TeamName) VALUES (?)", (userteam,))
                con.commit()

                loggedIn = True
                print(loggedIn)
                print(userteam)
                return redirect('/ctf')
        return render_template('login.html', error=error)
    else:
        return redirect('/ctf')


# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
