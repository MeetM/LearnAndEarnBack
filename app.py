from datetime import datetime

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os
import pprint

pp = pprint.PrettyPrinter(indent=4)
# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)



class Course(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(300))
  buy_in_start_date = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
  buy_in_end_date = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
  maturity_date = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)

  def __init__(self, name, buy_in_start_date, buy_in_end_date, maturity_date):
    self.name = name
    self.buy_in_start_date = buy_in_start_date
    self.buy_in_end_date = buy_in_end_date
    self.maturity_date = maturity_date

# Course Schema
class CourseSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'buy_in_start_date', 'buy_in_end_date', 'maturity_date')


# Init schema
course_schema = CourseSchema()
courses_schema = CourseSchema(many=True)



class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(300), unique=True)
  eth_address = db.Column(db.String(300), unique=True)

  def __init__(self, name, email, eth_address):
    self.name = name
    self.email = email
    self.eth_address = eth_address

# User Schema
class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'email', 'eth_address')





# Get All Courses
@app.route('/course', methods=['GET'])
def get_courses():
  all_courses = Course.query.all()
  result = courses_schema.dump(all_courses)
  return jsonify(result)

# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Create a User
@app.route('/user', methods=['POST'])
def add_user():
  name = request.json['name']
  email = request.json['email']
  eth_address = request.json['eth_address']
  new_user = User(name, email, eth_address)

  db.session.add(new_user)
  db.session.commit()

  return user_schema.jsonify(new_user)

# Get All Users
@app.route('/user', methods=['GET'])
def get_users():
  all_users = User.query.all()
  result = users_schema.dump(all_users)
  return jsonify(result)

# Get Single Products
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
  user = User.query.get(id)
  return user_schema.jsonify(user)

# Sign in
@app.route('/sign_in', methods=['POST'])
def add_sign_in():
  eth_address = request.json['eth_address']
  user_query = User.query.filter_by(eth_address=eth_address).all()
  result = users_schema.dump(user_query)
  pp.pprint(result)
  return jsonify(result)


if __name__ == '__main__':
  app.run(debug=True)