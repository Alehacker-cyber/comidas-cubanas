from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# ✅ Crea la instancia de Flask primero
app = Flask(__name__)

# ✅ Configura la app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'I love my mom'

# ✅ Importa e inicializa extensiones
from models import db, User, Order
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'routes.login'  # ✅ si usas Blueprint llamado 'routes'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ✅ Define rutas locales
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_language', methods=['POST'])
def set_language():
    lang = request.form.get('language')
    session['lang'] = lang
    return redirect(request.referrer or url_for('index'))

# ✅ Importa y registra Blueprint después de definir app
from routes import routes
app.register_blueprint(routes)

# ✅ Ejecuta localmente
if __name__ == '__main__':
    app.run(debug=True)
