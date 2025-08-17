from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from models import User, Order, Dish, db

routes = Blueprint('routes', __name__)

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('routes.dashboard'))
        else:
            flash('Credenciales incorrectas')
    return render_template('login.html')

@routes.route('/dashboard')
@login_required
def dashboard():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', orders=orders)

@routes.route('/order', methods=['GET', 'POST'])
@login_required
def order():
    if request.method == 'POST':
        dish = request.form['dish']
        quantity = int(request.form['quantity'])
        notes = request.form.get('notes')
        new_order = Order(dish=dish, quantity=quantity, notes=notes, user_id=current_user.id)
        db.session.add(new_order)
        db.session.commit()
        flash('¡Orden enviada con éxito!')
        return redirect(url_for('routes.dashboard'))
    return render_template('order.html')
@routes.route('/admin/dishes')
@login_required
def manage_dishes():
    if current_user.role != 'admin':
        return redirect(url_for('routes.dashboard'))
    dishes = Dish.query.all()
    return render_template('manage_dishes.html', dishes=dishes)

@routes.route('/admin/dishes/edit/<int:dish_id>', methods=['GET', 'POST'])
@login_required
def edit_dish(dish_id):
    if current_user.role != 'admin':
        return redirect(url_for('routes.dashboard'))
    dish = Dish.query.get_or_404(dish_id)
    if request.method == 'POST':
        dish.name = request.form['name']
        dish.description = request.form['description']
        dish.price = float(request.form['price'])
        dish.image_url = request.form['image_url']
        db.session.commit()
        flash('Plato actualizado')
        return redirect(url_for('routes.manage_dishes'))
    return render_template('edit_dish.html', dish=dish)
