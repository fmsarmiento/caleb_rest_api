from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///data.db' # Create an sqlite database of data.db in the same directory
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description} [{self.id}]"

# Create an endpoint and path
@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks') # 127.0.0.1:5000/drinks
def get_drinks():
    drinks = {"drinks": "drink data"}
    return drinks

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return ({"name": drink.name, "description":drink.description})

@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}

@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink():
    drink = Drink.query.get(id)
    if drink is None:
        return{"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "Ok"}