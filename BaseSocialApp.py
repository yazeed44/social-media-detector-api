from abc import ABC, abstractmethod


class BaseSocialApp(ABC):

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def detect_single_number(self, phone_number):
        pass

    @abstractmethod
    def detect_numbers(self, phone_numbers):
        pass
