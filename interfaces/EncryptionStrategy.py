from abc import ABC, abstractmethod

class EncryptionStrategy(ABC):
    @abstractmethod
    def obscure_secret(self, item):
        pass

    @abstractmethod
    def get_secret(self, item):
        pass

    @abstractmethod
    def store_secret(self, item):
        pass

