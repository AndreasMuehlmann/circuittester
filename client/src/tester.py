from abc import ABC, abstractmethod

class TesterException(Exception):
    pass


class Tester(ABC):
    @abstractmethod
    def test(self):
        pass
