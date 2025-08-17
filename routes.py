from models import Order, db
from flask_login import current_user

@app.route('/order', methods=['GET', 'POST'])
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
        return redirect(url_for('dashboard'))
    return render_template('order.html')

@app.route('/orders')
@login_required
def orders():
    user_orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('orders.html', orders=user_orders)
