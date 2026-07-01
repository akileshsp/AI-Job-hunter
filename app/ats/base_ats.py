from abc import ABC, abstractmethod


class BaseATS(ABC):

    def __init__(self):

        self.name = self.__class__.__name__

    @abstractmethod
    def search(self, keyword, location):
        """
        Returns:
            List[Job]
        """
        pass