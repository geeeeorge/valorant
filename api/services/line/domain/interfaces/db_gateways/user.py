import abc

from ...user import User


class UserInterface(abc.ABCMeta):

    @abc.abstractmethod
    def create(self, user: User):
        pass

    @abc.abstractmethod
    def update(self, user: User):
        pass

    @abc.abstractmethod
    def retrieve(self, name: int):
        pass

    @abc.abstractmethod
    def delete(self, id: int):
        pass

    @abc.abstractmethod
    def list(self):
        pass

    @abc.abstractmethod
    def has(self, id: int):
        pass
