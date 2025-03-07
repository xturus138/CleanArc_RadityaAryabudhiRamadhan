from flask import Blueprint
from controllers import user_controller


user_routes = Blueprint('user_routes', __name__)
user_routes.route('/users', methods=['GET'])(user_controller.get_users)
user_routes.route('/users', methods=['POST'])(user_controller.create_user)