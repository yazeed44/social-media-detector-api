
from enum import Enum
from dataclasses import dataclass, field
class AppUsageEnum(Enum):
    ERROR = -1  # There was an error while trying to detect whether this phone number uses a certain social app.
    NO_USAGE = 0  # This phone number does not use the app
    USAGE = 1  # This phone number has the app and it uses it

@dataclass
class PhoneNumber:
    _phone_number: str = ""
     # Used to track which apps are used by this phone number
    app_usage: dict = field(init=False,default_factory=dict)

    # get a current phone number
    @property
    def phone_number(self) -> str:
        return self._phone_number

    # set a new phone number
    @phone_number.setter
    def phone_number(self, value: str) -> None:
        self._phone_number = value

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
            # to handle errors
            try:
                usage_as_string += key + " => " + val.name + "\n"
            except:
                usage_as_string += key + " => " + val + "\n"
        return usage_as_string

    def verifier(number) -> bool:
        '''
        Return boolean value based on the verification logic
            
            Parameters:
                number  -> the number need to be verified
            Return:
                True    -> if it's valid
                False   -> if it's not valid
        '''
        # TODO: substring condition
        if(len(number) == 10):
             return True
        else:
            return False