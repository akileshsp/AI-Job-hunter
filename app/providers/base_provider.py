from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def search(self):
        """Return a list of Job objects"""
        pass