
from enum import Enum


class AppUsageEnum(Enum):
    ERROR = -1  # There was an error while trying to detect whether this phone number uses a certain social app.
    NO_USAGE = 0  # This phone number does not use the app
    USAGE = 1  # This phone number has the app and it uses it


class PhoneNumber:

    # TODO include the usernames of each application in here
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.app_usage = {}  # Used to track which apps are used by this phone number

    def get_phone_number(self):
        return self.phone_number

    # Return a constant of AppUsageEnum
    def has_app(self, app_name):
        return self.app_usage[app_name]

    # Sets whether a phone number is using an app
    # state will be a constant of AppUsageEnum
    def set_app_state(self, app_name, state):
        self.app_usage[app_name] = state

    def __str__(self):
        usage_as_string = self.phone_number + "\n"
        for key, val in self.app_usage.items():
            usage_as_string += key + " => " + val.name + "\n"
        return usage_as_string
