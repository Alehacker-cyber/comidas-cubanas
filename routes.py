@routes.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        return redirect(url_for('routes.admin_dashboard'))
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard_cliente.html', orders=orders)

@routes.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        return redirect(url_for('routes.dashboard'))
    orders = Order.query.all()
    return render_template('dashboard_admin.html', orders=orders)
