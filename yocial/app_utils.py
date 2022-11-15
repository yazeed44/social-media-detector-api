"""Module docs"""
import os
from yocial.features.PhoneNumber import PhoneNumber


def file_to_phone_number(file_path):
    '''docs'''
    phone_number_list: list = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        for line in file:
            phone_number_list.append(PhoneNumber(line.strip("\n")))
    return phone_number_list


# Convert command line arguments to PhoneNumber objects.
# If the arguments is a file's name then that file will be
# processed and not the arguments themselves
def cmd_args_to_phone_number(arguments: str):
    '''docs'''

    # as a bypass for the time being until I develop verify function
    # I will incrment the condition to 2
    # as arguments[0] is always the project entry point `__main__.py`
    assert len(arguments) >= 2, "No arguments are provided"

    phone_number_list: list = []
    # checking if it's a file
    if os.path.isfile(arguments[1]):
        return file_to_phone_number(arguments[1])
    for raw_phone_number in arguments[1:]:
        # ensure PhoneNumber object initialize only for valid numbers
        verified = verifier(number=raw_phone_number)
        if verified:
            phone_number_list.append(PhoneNumber(raw_phone_number))
    return phone_number_list


def verifier(number: str) -> bool:
    """
    Return boolean value based on the verification logic

        Parameters:
            number  -> the number need to be verified
        Return:
            True    -> if it's valid
            False   -> if it's not valid
    """
    allowed_numbers: list = ["050", "053",
                             "054", "055", "056", "057", "058", "059"]
    if len(number) == 10 and number[:3] in allowed_numbers:
        return True
    return False
