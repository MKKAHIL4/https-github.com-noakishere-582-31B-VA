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

        if not username:
                flash("Username cannot be empty")
                return render_template("register.html")

        if not email:
            flash("Email cannot be empty")
            return render_template("register.html")

        if not password:
            flash("Password cannot be empty")
            return render_template("register.html")

        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()


        if existing_user:
            flash("Username or email already exist")
            return render_template("register.html")

        user = User(
            username=username,
            email=email
            )

        user.set_password(password)     
        db.session.add(user)
        db.session.commit()

        flash("Account Created Successfully")

        return redirect(url_for("home"))
            



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
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        note = request.form["note"].strip()
        status = request.form["status"]

        allowed_status = [
            "Want to read",
            "Reading",
            "Finished"
        ]
    
        if not title:
            flash("Title cannot be empty")
            return render_template("add_book.html")

        if len(title) > 100:
            flash("Title cannot be more than 100 characters")
            return render_template("add_book.html")

        if not author:
            flash("Author cannot be empty")
            return render_template("add_book.html")


        if len(author) > 100:
            flash("Author cannot be more than 100 characters")
            return render_template("add_book.html")

        if len(note) > 1000:
            flash("Note cannot be more than 100 characters")
            return render_template("add_book.html")

        if status not in allowed_status:
            flash("Invalid reading status")
            return render_template("add_book.html")   

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
       

@app.route("/books/<int:book_id>/edit", methods=["GET", "POST"])
@login_required
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)

    if book.user_id != current_user.id:
        flash("You are not allowed to edit this book ")
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        status = request.form["status"]

        allowed_status =[
            "Want to read",
            "Reading",
            "Finished"
        ]

        if status not in allowed_status:
            flash("Invalid reading status")
            return render_template(
                "book_edit.html",
                book=book
            )
        book.status = status

        db.session.commit()

        flash("Book Updated Successfully")

        return redirect(url_for("dashboard"))

    return render_template(
        "book_edit.html",
        book=book
    )  


@app.route("/books/<int:book_id>/delete", methods=["POST"])
@login_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)

    if book.user_id != current_user.id:
        flash("You are not allowed to delete this book ")
        return redirect(url_for("dashboard"))
    
    
    db.session.delete(book)
    db.session.commit()

    flash("Book Deleted Successfully")

    return redirect(url_for("dashboard"))  



with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
