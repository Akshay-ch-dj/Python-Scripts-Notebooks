from datetime import timedelta
from flask import (
    Flask,
    redirect,
    url_for,
    render_template,
    request,
    session,
    flash)

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "mongoose"
# DB configuration for sqlite3(users is the table name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
# Not track all db modifications(optional)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Set session lifetime
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)


# models using SQLAlchemy
class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def home():
    return render_template("index.html", content="Testing")


@app.route("/view")
def view():
    return render_template("view.html", values=Users.query.all())


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        # If the page is loaded with POST, name for the input
        user = request.form["nm"]
        session["user"] = user

        # check the db for user
        found_user = Users.query.filter_by(name=user).first()

        # Check if user exists, if doesn't create one
        if found_user:
            session['email'] = found_user.email
        else:
            # Create an instance of Users model
            # Don't have an email initially
            usr = Users(user, "")
            # Add the usr model to the database
            db.session.add(usr)
            db.session.commit()  # save it to db same as 'save' in django

        flash("Login Successful!", "info")
        # Just redirect to the user page
        return redirect(url_for("user"))
    else:
        # To get to the logged in page as long as the session data exists
        if "user" in session:
            flash("Already Logged In", "info")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    # Check if any session data exists, and login
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email

            # check the db for user(not the best soln. user already logged in)
            found_user = Users.query.filter_by(name=user).first()

            # save the entered email to the database
            found_user.email = email
            db.session.commit()

            flash("Email was saved", "info")
        else:
            if "email" in session:
                email = session["email"]
        # Render the template with user value passed in
        return render_template("user.html", email=email)
    # If not valid session data, redirect back to the login page
    else:
        flash("You are not logged in!", "info")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Check if the user logged in or not then display the flash message
    if "user" in session:
        user = session["user"]
        flash(f"You have been successfully logged out, {user}", "info")

    # For clearing out the session data
    session.pop("user", None)
    session.pop("email", None)
    # Redirect to login page after that
    return redirect(url_for("login"))


# Run in debug mode
if __name__ == "__main__":
    # Create the database it doesn't exist
    db.create_all()
    app.run()
