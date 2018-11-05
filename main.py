from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config ['DEBUG'] = True

@app.route("/")
def index ():
    return render_template('login.html')


@app.route("/", methods=['POST'])
def signup():

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    #validate username
    if username == "":
        username_error = "Username required"
    elif len(username) <= 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters in length."
        username = ""
    elif " " in username:
        username_error = "Username cannot contain spaces."
        username = ""

    #validate password
    if password == "":
        password_error = "Please enter a valid password."
    elif len(password) <= 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters in length."
        password = ""
    elif " " in password:
        password_error = "Your password cannot contain spaces."
        password = ""

    #verify password
    if verify == "" or verify != password:
        verify_error = "Passwords do not match. Please try again"
        verify = ""

    #validate email using re
    if email != "":
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            email_error = "Not a valid email address."

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('successful.html', username = username)
    else:
        return render_template(
        'login.html',
        username = username,
        username_error = username_error,
        password_error = password_error,
        verify_error = verify_error,
        email = email,
        email_error = email_error
        )

app.run()