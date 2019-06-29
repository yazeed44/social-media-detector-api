from telethon import TelegramClient, sync
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact

from BaseSocialApp import BaseSocialApp

import os.path

from PhoneNumber import AppUsageEnum


class Telegram(BaseSocialApp):
    # Two lists of authenticators, and will be checked to assure that they are of the same length
    api_ID = None
    api_hash = None

    def __init__(self, phone_numbers_to_detect, api_id, api_hash):
        self.api_ID = api_id
        self.api_hash = api_hash
        super().__init__(phone_numbers_to_detect)

    def authenticate(self):
        # detect.session file is a file used by Telegram API to keep current sessions going
        # TODO implement a method to have multiple sessions
        if not os.path.isfile("detect.session"):
            print("Telegram will need authorization into your account")

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
                    # If the user's id is not 0 then the user has an account in Telegram
                    phone_number.set_app_state(self.get_name(),
                                               AppUsageEnum.USAGE if contact.user_id > 0 else AppUsageEnum.NO_USAGE)

                except ValueError as e:
                    # TODO Use an error logger
                    # print(e)
                    phone_number.set_app_state(self.get_name(), AppUsageEnum.ERROR)
        return phone_numbers

    def process(self):
        # TODO implement an optimal algorithm for Telegram where various client phone numbers are used to detect
        self.detect_numbers(self.phone_numbers_to_detect)

    def get_name(self):
        return "Telegram"
