from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import db, User, Order, Dish  # si ya agregaste Dish

app = Flask(__name__)

# ✅ Cargar configuración desde config.py
app.config.from_object('config.Config')

# ✅ Inicializar extensiones
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'routes.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Rutas locales
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_language', methods=['POST'])
def set_language():
    lang = request.form.get('language')
    session['lang'] = lang
    return redirect(request.referrer or url_for('index'))

# Registrar blueprint
from routes import routes
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
