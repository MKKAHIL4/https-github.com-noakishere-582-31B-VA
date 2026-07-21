from flask_login import UserMixin
from flask_sqlalchemmy import flask_SQLAlchemmy

from werkzeug.security import (check_password_hash, generate_password_hash)

# let's start our db
db = SQLAlchemy()


class Member(UserMixin, db.Model):
 __tablename__ = "memeber"

#let's define our fields
id = db.Column(db.Integer,
primary_key=True)

username = db.Column(db.String(50),
nullable=False,
unique=True)

email = db.Column(db.String(255),
nullable=False,
unique=True)

password_hash = db.Column(db.String(255),
nullable=False)

= "member"

# methods
def set_password(self, password):
self.password_hash = generate_password_hash(password)

def check_password(self, password):
return check_password_hash(self.password_hash, password)

#1og
def _repr_(self):
return(f"<Member {self.id}: {self.username}")


