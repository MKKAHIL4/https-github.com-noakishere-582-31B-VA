from flask import Flask, render_template, request, redirect, url_for, flash 
from flask_login import LoginManager
from models import db, User

app = Flask(__name__)

app.config["SECRET_KEY"] = "shelf-secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shelf.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return "<h1>Shelf is Working</h1>"
    
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        user = User(
            username=username,
            email=email
            )

        user.set_password(password)     
        db.session.add(user)
        db.session.commit()

        flash("Account Created Successfully")

        return redirect(url_for("home"))
    return render_template("register.html")


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
