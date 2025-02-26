from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import random

app = Flask(__name__)
app.secret_key = "eaglestx_secret_key"

# Database setup (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eaglestx.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(10), default="user")  # "admin" or "user"

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Load user for authentication
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home Route
@app.route('/')
def home():
    return "Welcome to EaglesTX Backend API"

# User Authentication
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        login_user(user)
        return jsonify({"message": "Login Successful", "role": user.role})
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"})

# Fetch Products
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [{"id": p.id, "name": p.name, "price": p.price} for p in products]
    return jsonify(product_list)

# Payment Processing
@app.route('/payment', methods=['POST'])
@login_required
def process_payment():
    data = request.json
    payment_method = data['method']
    amount = data['amount']

    # Simulated Payment Response
    if random.choice([True, False]):  # Simulating success or failure
        return jsonify({"message": "Payment Successful", "status": "success"})
    return jsonify({"message": "Payment Failed", "status": "failed"})

# Admin Routes
@app.route('/admin/add_product', methods=['POST'])
@login_required
def add_product():
    if current_user.role != "admin":
        return jsonify({"message": "Unauthorized"}), 403
    
    data = request.json
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product added successfully"})

@app.route('/admin/delete_user', methods=['DELETE'])
@login_required
def delete_user():
    if current_user.role != "admin":
        return jsonify({"message": "Unauthorized"}), 403

    data = request.json
    user = User.query.get(data['user_id'])
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"})
    return jsonify({"message": "User not found"}), 404

# FAQs
faqs = [
    {"question": "What is EaglesTX?", "answer": "EaglesTX is an internet and networking service provider."},
    {"question": "How can I pay?", "answer": "You can use Bank Transfer, MPESA, or Binance."},
]

@app.route('/faqs', methods=['GET'])
def get_faqs():
    return jsonify(faqs)

# Run Flask App
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure database is created
    app.run(debug=True)
