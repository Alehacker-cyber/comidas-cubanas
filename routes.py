from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from models import User, Order, db

routes = Blueprint('routes', __name__)

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

@routes.route('/dashboard')
@login_required
def dashboard():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', orders=orders)
