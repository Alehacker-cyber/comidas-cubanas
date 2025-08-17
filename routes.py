from models import User  # Asegúrate de importar tu modelo de usuario

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
