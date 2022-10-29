import os

from yocial.features.PhoneNumber import PhoneNumber


def file_to_phone_number(file_path):
    phone_number_list = []
    with open(file_path) as file:
        for line in file:
            phone_number_list.append(PhoneNumber(line.strip('\n')))
    return phone_number_list

# Convert command line arguments to PhoneNumber objects. If the arguments is a file's name then that file will be
# processed and not the arguments themselves
def cmd_args_to_phone_number(arguments):
    
    # Currently the processing of numbers to objects is sensitive. Meaning that empty and invalid lines might get
    # processed into an objects, which obviously shouldn't. Bear that in mind

    # as a bypass for the time being until I develop verify function I will incrment the condition to 2
    # as arguments[0] is always the project entry point `__main__.py`
    assert len(arguments) >= 2, "No arguments are provided"
    
    phone_number_list = []
    if os.path.isfile(arguments[1]):
        return file_to_phone_number(arguments[1])
    else:
        for raw_phone_number in arguments[1:]:
            # ensure PhoneNumber object initialize only for valid numbers
            verified = PhoneNumber.verifier(number=raw_phone_number)
            if(verified):
                phone_number_list.append(PhoneNumber(raw_phone_number))
    return phone_number_list
