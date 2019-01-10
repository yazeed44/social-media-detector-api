import sys

from telethon import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact

import private_constants


def check_telegram(phone_number):
    with TelegramClient('detect', private_constants.TELEGRAM_API_ID, private_constants.TELEGRAM_API_HASH) as client:
        contact = InputPhoneContact(client_id=0, phone=phone_number, first_name=phone_number, last_name='cba')
        result = client(ImportContactsRequest([contact]))  # TODO Import phone numbers as a whole to save time
        try:
            contact = client.get_input_entity(phone_number)
            user_id = contact.user_id
            return user_id > 0

        except ValueError:
            # TODO Use an error logger
            return False


def main():
    for phoneNumber in sys.argv[1:]:
        has_telegram = check_telegram(phoneNumber)
        print(has_telegram)


if __name__ == "__main__":
    main()
