from flask.ext.login import LoginManager
from application.models.user import Users


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return Users.objects(id=user_id).first()

login_manager.login_view = "frontend.login"
