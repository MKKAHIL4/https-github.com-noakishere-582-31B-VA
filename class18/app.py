# IMPORTANT: never name your file flask.py

from flask import Flask # import flask

app = Flask(__name__) # create the application object.
#name_ is commonly used here so Flask knows where to look for resources.

# associate the URL path with the function below.
# this decorator tells Flask what URL should trigger the function.
@app.route("/")
def hello():
    return "<h1>Hello, Flask !</h1>" # returns the response sent to the browser.

@app.route("/about")
def about():
    return "<h1>About</h1> <p>This is the about page .< /p>"

@app.route("/contact")
def contact():
    return "<h1>Contact</h1> <p>Contact us here./p>"

