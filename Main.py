# TODO investigate limitations of Telegram API regarding importing contacts
# TODO allow users to specify which social media application to track
# TODO Write unit tests
# TODO Write documentation
import os.path
import sys
import private_constants
from PhoneNumber import PhoneNumber
from Telegram import Telegram
from Whatsapp import Whatsapp


def create_phone_numbers(arguments):
    # Currently the processing of numbers to objects is sensitive. Meaning that empty and invalid lines might get
    # processed into an objects, which obviously shouldn't. Bear that in mind

    if len(arguments) <= 1:
        return []

    phone_number_list = []
    if os.path.isfile(arguments[1]):
        with open(arguments[1]) as file:
            for line in file:
                phone_number_list.append(PhoneNumber(line.strip('\n')))
    else:
        for raw_phone_number in arguments[1:]:
            phone_number_list.append(PhoneNumber(raw_phone_number.strip('\n')))
    return phone_number_list


def main():
    phone_number_list = create_phone_numbers(sys.argv)
    assert phone_number_list != [], "The input is empty"
    Telegram(private_constants.TELEGRAM_API_ID, private_constants.TELEGRAM_API_HASH).detect_numbers(phone_number_list)
    Whatsapp().detect_numbers(phone_number_list)
    for number in phone_number_list:
        print(number)


if __name__ == "__main__":
    main()
