from flask import Flask, render_template, request, redirect, url_for, flash 
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Book

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
    return render_template("home.html")
    
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



@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            
            flash("Login Successfully")

            return redirect(url_for("home")) 
        flash("Invalid email or password")

    return render_template("login.html")

@app.route("/logout")
def logout():
    
    logout_user()
    
    flash("Logged out successfully")    
    
    return redirect(url_for("home"))

@app.route("/dashboard")
@login_required
def dashboard():

    books = Book.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "dashboard.html",
        username=current_user.username,
        books=books
        )

@app.route("/add_book", methods=["GET", "POST"])
@login_required
def add_book():

    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        note = request.form["note"]
        status = request.form["status"]

        book = Book(
            title=title,
            author=author,
            note=note,
            status=status,
            user_id=current_user.id

        ) 

        db.session.add(book)

        db.session.commit()
           
        flash("Book loaded successfully")

        return redirect(url_for("dashboard")) 

    return render_template("add_book.html")




with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
