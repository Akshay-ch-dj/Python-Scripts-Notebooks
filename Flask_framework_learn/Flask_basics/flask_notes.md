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

### Displaying Dynamic information

* To pass information from backend flask to html, python jinja language is also used here, so for example if a `<p>{{ content }}</p>` is in the `index.html`, and the information comes from the `render_template` as content.

  ```py
  @app.route("/<n>")
  def home(name):
      return render_template("index.html", content=name)
  ```

* Now the template `p` will be rendered with the dynamic content given,