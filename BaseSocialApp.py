from abc import ABC, abstractmethod


class BaseSocialApp(ABC):
    # These numbers will be looking to detect whether it is using a certain application or not
    phone_numbers_to_detect = None

    def __init__(self, phone_numbers_to_detect):
        self.phone_numbers_to_detect = phone_numbers_to_detect

    @abstractmethod
    def authenticate(self):
        pass

    # TODO Find a way to separate detection & authentication into a new class
    @abstractmethod
    def detect_single_number(self, phone_number):
        pass

    @abstractmethod
    def detect_numbers(self, phone_numbers):
        pass

    @abstractmethod
    def process(self):
        # This method is the highest of the order in here. It will be called by SocialDetector to start the whole
        # detecting process For example, say you wanted to you know if 100k phone number are using Whatsapp. You
        # would use this method to divide those phone numbers among the phone numbers you are using to detect
        pass

    @abstractmethod
    def get_name(self):
        # Each social media app would have a unique name that would be used to identify it
        pass
