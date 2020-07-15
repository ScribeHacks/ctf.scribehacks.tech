from flask import Flask, request, render_template, redirect, url_for
import os
from dotenv import load_dotenv
load_dotenv()
# from datetime import datetime

app = Flask(__name__)
loggedIn = False


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
            if request.form['username'] != 'admin' or request.form['password'] != 'admin':
                error = 'Invalid Credentials. Please try again.'
            else:
                loggedIn = True
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