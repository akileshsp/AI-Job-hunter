from abc import ABC, abstractmethod


class BaseJobSource(ABC):

    @abstractmethod
    def search(self, keyword="", location=""):
        """
        Return a list of Job objects.
        """
        pass