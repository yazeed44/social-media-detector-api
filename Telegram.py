from telethon import TelegramClient, sync
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact

from BaseSocialApp import BaseSocialApp

import os.path


class Telegram(BaseSocialApp):
    api_ID = None
    api_hash = None

    def __init__(self, api_id, api_hash):
        self.api_ID = api_id
        self.api_hash = api_hash
        super().__init__()

    def authenticate(self):
        # detect.session file is a file used by Telegram API to keep current sessions going
        if not os.path.isfile("detect.session"):
            print("Telegram will need authorization into your account. Ignore this message if it skips to Whatsapp's "
                  "bar code scan")

    def detect_single_number(self, phone_number):
        self.detect_numbers([phone_number])

    def detect_numbers(self, phone_numbers):
        self.authenticate()
        with TelegramClient('detect', self.api_ID, self.api_hash) as client:
            input_contact_list = []
            for phone_number in phone_numbers:
                input_contact_list.append(
                    InputPhoneContact(client_id=0, phone=phone_number.get_phone_number(),
                                      first_name=phone_number.get_phone_number(),
                                      last_name=phone_number.get_phone_number()))
            client(ImportContactsRequest(input_contact_list))
            for phone_number in phone_numbers:
                try:
                    contact = client.get_input_entity(phone_number.get_phone_number())
                    phone_number.set_telegram(contact.user_id > 0)

                except ValueError as e:
                    # TODO Use an error logger
                    # print(e)
                    phone_number.set_telegram(False)
        return phone_numbers
