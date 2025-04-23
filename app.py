from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food_recommendation.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    health_condition = db.Column(db.String(200))
    address = db.Column(db.Text)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    health_benefits = db.Column(db.String(200), nullable=False)
    suitable_for = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    meal_type = db.Column(db.String(20), nullable=False)  # breakfast, lunch, or dinner
    
    def __repr__(self):
        return f'<FoodItem {self.name}>'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_item.id'), nullable=False)
    food_name = db.Column(db.String(100), nullable=False)
    food_image = db.Column(db.String(500))
    quantity = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Pending')
    delivery_address = db.Column(db.Text)
    total_price = db.Column(db.Float, nullable=False)
    
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    food_item = db.relationship('FoodItem', backref=db.backref('orders', lazy=True))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Initialize cart in session
@app.before_request
def before_request():
    if 'cart' not in session:
        session['cart'] = []

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        health_condition = request.form.get('health_condition')
        address = request.form.get('address')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
            
        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return redirect(url_for('register'))
            
        user = User(username=username, email=email, health_condition=health_condition, address=address)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('cart', None)
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    # Get recommended foods grouped by meal type
    recommended_foods = {
        'breakfast': FoodItem.query.filter(
            FoodItem.suitable_for.like(f'%{current_user.health_condition}%'),
            FoodItem.meal_type == 'breakfast'
        ).all(),
        'lunch': FoodItem.query.filter(
            FoodItem.suitable_for.like(f'%{current_user.health_condition}%'),
            FoodItem.meal_type == 'lunch'
        ).all(),
        'dinner': FoodItem.query.filter(
            FoodItem.suitable_for.like(f'%{current_user.health_condition}%'),
            FoodItem.meal_type == 'dinner'
        ).all()
    }
    return render_template('dashboard.html', foods=recommended_foods)

@app.route('/add_to_cart/<int:food_id>', methods=['POST'])
@login_required
def add_to_cart(food_id):
    food = FoodItem.query.get_or_404(food_id)
    quantity = int(request.form.get('quantity', 1))
    
    cart_item = {
        'food_id': food.id,
        'name': food.name,
        'price': food.price,
        'quantity': quantity,
        'image_url': food.image_url
    }
    
    # Check if item already in cart
    for item in session['cart']:
        if item['food_id'] == food_id:
            item['quantity'] += quantity
            break
    else:
        session['cart'].append(cart_item)
    
    session.modified = True
    flash(f'{food.name} added to cart!')
    return redirect(url_for('dashboard'))

@app.route('/cart')
@login_required
def cart():
    cart_items = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/remove_from_cart/<int:item_id>', methods=['POST'])
@login_required
def remove_from_cart(item_id):
    cart_items = session.get('cart', [])
    for i, item in enumerate(cart_items):
        if item['food_id'] == item_id:
            cart_items.pop(i)
            session['cart'] = cart_items
            session.modified = True
            flash('Item removed from cart')
            break
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    cart_items = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    
    if request.method == 'POST':
        address = request.form.get('address')
        if not address:
            flash('Please provide a delivery address')
            return redirect(url_for('checkout'))
        
        if not cart_items:
            flash('Your cart is empty')
            return redirect(url_for('cart'))
        
        for item in cart_items:
            food = FoodItem.query.get(item['food_id'])
            order = Order(
                user_id=current_user.id,
                food_item_id=food.id,
                food_name=food.name,
                food_image=food.image_url,
                quantity=item['quantity'],
                delivery_address=address,
                total_price=item['price'] * item['quantity']
            )
            db.session.add(order)
        
        db.session.commit()
        session['cart'] = []
        flash('Order placed successfully!')
        return redirect(url_for('order_history'))
    
    return render_template('checkout.html', cart_items=cart_items, total=total)

@app.route('/order_history')
@login_required
def order_history():
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.order_date.desc()).all()
    return render_template('order_history.html', orders=orders)

@app.route('/track_order/<int:order_id>')
@login_required
def track_order(order_id):
    order = Order.query.get_or_404(order_id)
    if order.user_id != current_user.id:
        flash('You are not authorized to view this order')
        return redirect(url_for('order_history'))
    return render_template('track_order.html', order=order)

@app.route('/order_food/<int:food_id>', methods=['POST'])
@login_required
def order_food(food_id):
    food = FoodItem.query.get_or_404(food_id)
    quantity = int(request.form.get('quantity', 1))
    
    if 'cart' not in session:
        session['cart'] = []
    
    cart_item = {
        'food_id': food.id,
        'name': food.name,
        'price': food.price,
        'quantity': quantity,
        'image_url': food.image_url
    }
    
    # Check if item already in cart
    for item in session['cart']:
        if item['food_id'] == food_id:
            item['quantity'] += quantity
            break
    else:
        session['cart'].append(cart_item)
    
    session.modified = True
    flash(f'{food.name} added to cart!')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 