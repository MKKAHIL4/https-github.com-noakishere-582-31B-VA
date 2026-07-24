from flask import Flask 
from flask_login import LoginManager
from models import db, User

app = Flask(__name__)

app.config["SECRET_KEY"] = "shelf-secret-key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shelf.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = db

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(init(user_id))

@app.route("/")
def home():
    return "<h1>Shelf is Working</h1>"

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
