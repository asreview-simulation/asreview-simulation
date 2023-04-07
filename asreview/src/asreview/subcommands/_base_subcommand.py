from abc import abstractmethod
from abc import ABC


class BaseSubcommand(ABC):

    @abstractmethod
    def __call__(self, argv):
        pass
