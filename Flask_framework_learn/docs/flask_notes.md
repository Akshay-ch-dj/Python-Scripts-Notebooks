# Flask basics

---

<!-- ![flask](https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png) -->

* Micro-framework for building websites with python.
* Start with `pip install flask`.

## First run

* create a python file [first_burn.py].
* import flask. create an instance of the web application, look here, [first_burn.py](./first_burn.py)

  ```py
  from flask import Flask

  # Instance of the flask web app
  app = Flask(__name__)

  # Run the app
  if __name__ == "__main__":
      app.run()

  ```

* The project is created and running now it is needed to define the pages for the website, the pages created using simple python functions.
* Just starting the homepage by returning an inline html.
* Use python decorators do define how the page can be accessed, ie route the page with `@app.route("/")`, "/" just means the home page, one can use "/home"..etc for the path.

  ```py
  @app.route("/")
  def home():
      return "Hello world, <h1>the main page</h1>"

  ```

* Then run the server, by running the .py file, that will run your first flask page.

  ```bash
  * Serving Flask app "first_burn" (lazy loading)
  * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
  * Debug mode: off
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```

* If we go to other undefined routes etc, `/home`, we get a 404 error.

## Pass a value as function parameter

* In routing, if the `@app.route("")` is called with a parameter, that will get passed to the function.

  ```py
  @app.route("/<name>")
  def user(name):
      return f'Hello {name}'
  ```

* Stop the server and rerun, then a `http://127.0.0.1:5000/akshay`, will gives 'Hello akshay' in the resulting page.

## Redirect pages

* If we need page that can be only acced by admins,
* Import the `redirect` and `url_for` from flask, the `url_for` accepts a function, ie which the redirect is to be done("Inside a quote").

  ```py
  from flask import Flask, redirect, url_for

  @app.route("/admin")
  def admin():
      return redirect(url_for("home"))
  ```

* Now the user will get redirected to the home page if enters `http://127.0.0.1:5000/admin`.
* If we want redirect with passing a value to that page function(which is the normal case), here the user function accepts an argument, to call the user with this value "Access prohibited!".

  ```py
  @app.route("/<name>")
  def user(name):
      return f'Hello {name}'

  @app.route("/admin")
  def admin():
      return redirect(url_for("user", name="Access prohibited!"))
  ```

Note:- The `route("/admin")` and `route("/admin/")` are different, the second one allows to route with both `/admin` and `/admin/`, with the first `/admin/` gives a no route error.

## ADDING OWN HTML TEMPLATES

* To render an html page import, `render_template` module from flask.
* Creates a new `./templates` directory in the same root as the app.py exists, and fill it with the desired html file(also incorporated with the combined css and js).
* Then just use that name of the html file with `render_template` (here index.html), like this,

  ```py
  from flask import Flask, redirect, url_for, render_template

  @app.route("/")
  def home():
      return render_template("index.html")
  ```

## Displaying Dynamic information

* To pass information from backend flask to html, python jinja language is also used here, so for example if a `<p>{{ content }}</p>` is in the `index.html`, and the information comes from the `render_template` as content.

  ```py
  @app.route("/<n>")
  def home(name):
      return render_template("index.html", content=name)
  ```

* Now the template `p` will be rendered with the dynamic content given, also can write the python logics with {% for %} {% endfor %} and {% if %} {% endif %} etc.

## Adding Bootstrap and template inheritance

* Look at the [python script](../Flask_basics/flsk_template_inheritance.py).
* In order to not repeating the html code..or imports, can use the template inheritance, create a `base.html` that can be used to inherit the basic contents to other pages.

* Setup blocks for other contents with `{% block <name> %} {% endblock <name> %}` for example for different titles for each page, use `{% block title %} {% endblock title %}` in the `<title>` tag, and another blocks like, `{% block content %} {% endblock content %}` for other blocks, then extend the base.html to other files using `{% extends 'base.html' %}`

## HTTP Methods and retrieving form Data

* Look at the [python script](../Flask_basics/flsk_template_inheritance.py).
* Here only the name input field gets fetched using the `request.form[]` (which is a dictionary that contains all the form inputs with keys as the names)(here `request.form["nm"]` gives the name input), then redirects to the user view(or route) using `url_for` with the fetched form data.

## Sessions in Flask

### Setting up the session

* Sessions are temporary credential data stored on the server, which is used to pass in the fetched data(login details) between different pages require them (`@login_required` mixin in django), or can use the session data.
* The previous example can be done using sessions, where the user logs in (gives the name) and that data can be stored in a session and can be used in the `user` page without direct passing.
* For that import `session` from flask, then use the session[], to set up the required data(as simple as setting up a dictionary), like `session["user"] = user`.
* In order to use the session, the session data needs to be encrypted with session key. SO use an `app.secrect_key = "dkjlsduikj"`(any string).
* And if the session data is not found, one can set to redirect to the login page again.
* View the code [here](../Flask_basics/sessions.py)

### Clearing the session

* Create a new logout route, one can remove the data from the session using the `session.pop()`, then redirect to the required page, [view](../Flask_basics/sessions.py).

### Permanent session

* One can set how long does the session data have to be stored, for that, to set the time import the datetime module (`from datetime import timedelta`), then to store it for eg, 5 days, use `app.permanent_session_lifetime = timedelta(days=5)`, or so `timedelta(minutes=5)` for 5 minutes.
* Also need to define the current session is permanent in each route(or globally, in each route gives more control), by setting ``
* View the code [here](../Flask_basics/sessions.py)

## Message Flashing

* Like alerts in the Django, If logged in successfully show, logged in successfully message as a flash, feedback and interaction with pages,
* Similarly import `flash` from `flask`, if needed to display the `logged out` message, use simply `flash("You have been logged out", "info")` (category:- warning, info and error)

## SQLAlchemy ORM to connect to Database

* View the code [here](../Flask_basics/dtabases_flask.py)
* Instal the sqlalchemy for flask, `pip install flask-sqlalchemy`, `from flask_sqlalchemy import SQLAlchemy`
* The `user.html` now setup to receive the user email as the input with `POST` method, also change the user route function methods to `"GET", "POST"`.
* The two things here needed to do with db are, in the login page, check if the user exists in the database if not add him to the database, if the user found grab his email and add to the session storage(that one gets auto inputted to the vale of the email input)
* The second thing is when a new user post their email, save to the db.
* To delete an item from the database, with an id, (also can be done with name or email, for multiple outs do a `.all()` and with a for loop delete all)

  ```py
  select_user = Users.query.filter_by(id=5).delete()
  db.session.commit()
  ```

* To view the saved items create a `view.html`, and corresponding route with all data sent (`values=Users.query.all()`), then in the html-using jinja loop through it and display all data.
