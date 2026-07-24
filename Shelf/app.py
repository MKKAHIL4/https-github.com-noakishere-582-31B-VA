from flask import Flask 
from models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shelf.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = db

db.init_app(app)

@app.route("/")
def home():
    return "<h1>Shelf is Working</h1>"

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
