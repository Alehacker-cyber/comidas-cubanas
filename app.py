from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import db, User  # Importa la instancia db y el modelo User

app = Flask(__name__)

# Configuración directa
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'I love my mom'

# Inicializa extensiones
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Define cómo cargar un usuario desde su ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Rutas principales
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_language', methods=['POST'])
def set_language():
    lang = request.form.get('language')
    session['lang'] = lang
    return redirect(request.referrer or url_for('index'))

# Importa rutas adicionales (si tienes más en routes.py)
try:
    import routes
except ImportError:
    pass  # Evita errores si aún no has creado routes.py

# Ejecuta localmente con debug
if __name__ == '__main__':
    app.run(debug=True)
