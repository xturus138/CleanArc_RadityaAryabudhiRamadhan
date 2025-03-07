from abc import ABC, abstractmethod
from domain.user import UserEntity


class UserRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass
    @abstractmethod
    def create(self, user: UserEntity):
        pass