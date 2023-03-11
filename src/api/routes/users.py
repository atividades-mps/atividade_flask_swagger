from flask import Blueprint

from src.api.services.mock_users_service import MockUsersService
from src.domain.use_cases.fetch_all_users import FetchAllUsers

users_blueprint = Blueprint('users', __name__)

@users_blueprint.get('/users')
def fetch_all():
    fetch_all_users = FetchAllUsers(MockUsersService())
    return fetch_all_users.execute()
