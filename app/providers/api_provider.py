from abc import ABC, abstractmethod


class APIProvider(ABC):

    def __init__(self):
        self.name = self.__class__.__name__

    @abstractmethod
    def search(self):
        """
        Returns a list of Job objects
        """
        pass

    def log(self):
        print(f"🌐 Searching from {self.name}...")