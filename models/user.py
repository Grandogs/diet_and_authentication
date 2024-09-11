from database import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
  # id (int), username (text), password (text)
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), nullable=False, unique=True)
  password = db.Column(db.String(80), nullable=False)
  mealName = db.Column(db.String(80), default=None)
  discretion = db.Column(db.String(80), default=None)
  dateAndTime = db.Column(db.DateTime)
  insideTheDiet = db.Column(db.Boolean, default=False)