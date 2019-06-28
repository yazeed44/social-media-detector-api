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

    @abstractmethod
    def process(self, phone_numbers):
        # This method is the highest of the order in here. It will be called by SocialDetector to start the whole
        # detecting process For example, say you wanted to you know if 100k phone number are using Whatsapp. You
        # would use this method to divide those phone numbers among the phone numbers you are using to detect
        pass
