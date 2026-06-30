from abc import ABC, abstractmethod


class BaseJobSource(ABC):

    @abstractmethod
    def search(self, keyword, location):
        pass