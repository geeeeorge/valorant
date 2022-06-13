from .interfaces.db_gateways.user import UserInterface
from .user import User


class UserRepository:

    db_gateway: UserInterface

    @classmethod
    def save(cls, user: User) -> None:
        if cls.db_gateway.has(user.id):
            cls.db_gateway.update(user)
        else:
            cls.db_gateway.create(user)

    @classmethod
    def search_by(cls, name: str) -> User:
        return cls.db_gateway.retrieve(name)

    @classmethod
    def delete(cls, id: int) -> None:
        return cls.db_gateway.delete(id)

    @classmethod
    def list(cls) -> list[User]:
        return cls.db_gateway.list()
