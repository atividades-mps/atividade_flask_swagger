from src.domain.entities.user import User
from src.domain.ports.users_service import UsersService


class MockUsersService(UsersService):
    def fetch_all(self) -> list[User]:
        return []