"""docs"""
import os.path
from telethon import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact
from yocial.features.PhoneNumber import AppUsageEnum
from yocial.features.BaseSocialApp import BaseSocialApp


class Telegram(BaseSocialApp):
    """docs"""
    # Two lists of authenticators, and will be checked to assure that they are
    # of the same length

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
        with TelegramClient("detect", self.api_ID, self.api_hash) as client:
            input_contact_list = []
            for phone_number in phone_numbers:
                input_contact_list.append(
                    InputPhoneContact(
                        client_id=0,
                        phone=phone_number.get_phone_number(),
                        first_name=phone_number.get_phone_number(),
                        last_name=phone_number.get_phone_number(),
                    )
                )
            client(ImportContactsRequest(input_contact_list))
            for phone_number in phone_numbers:
                try:
                    contact = client.get_input_entity(
                        phone_number.get_phone_number())
                    # If the user's id is not 0 then the user has an account in
                    # Telegram
                    phone_number.set_app_state(
                        self.get_name(),
                        AppUsageEnum.USAGE
                        if contact.user_id > 0
                        else AppUsageEnum.NO_USAGE,
                    )

                except ValueError as e:

                    # TODO Use an error logger
                    if "Cannot find any entity corresponding to" in str(e):
                        # If this error happens that means the API call was successfully, but the phone number does
                        # not have Telegram
                        phone_number.set_app_state(
                            self.get_name(), AppUsageEnum.NO_USAGE
                        )
                    else:
                        print(e)
                        phone_number.set_app_state(
                            self.get_name(), AppUsageEnum.ERROR)
        return phone_numbers

    def process(self):
        # TODO implement an optimal algorithm for Telegram where various client
        # phone numbers are used to detect
        self.detect_numbers(self.phone_numbers_to_detect)

    def get_name(self):
        return "Telegram"
