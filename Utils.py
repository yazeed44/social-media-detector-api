import os

from PhoneNumber import PhoneNumber


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

    assert len(arguments) >= 1, "No arguments are provided"

    phone_number_list = []
    if os.path.isfile(arguments[1]):
        return file_to_phone_number(arguments[1])
    else:
        for raw_phone_number in arguments[1:]:
            phone_number_list.append(PhoneNumber(raw_phone_number))
    return phone_number_list
