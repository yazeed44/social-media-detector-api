import hashlib
import hmac
import json
import urllib.parse

import uuid as uuid

import requests

import PhoneNumber
from BaseSocialApp import BaseSocialApp

API_URL = 'https://i.instagram.com/api/v1/'
USERS_LOOKUP_URL = API_URL + 'users/lookup/'
SIG_KEY_VERSION = '4'
IG_SIG_KEY = 'e6358aeede676184b9fe702b30f4fd35e71744605e39d2181a34cede076b3c33'


def generate_uuid(type):
    gen_uuid = str(uuid.uuid4())
    return gen_uuid if type else gen_uuid.replace('-', '')


def generate_device_id():
    return str(uuid.uuid4()).replace('-', '')[:17]


def generate_signature(data):
    return 'ig_sig_key_version=' + SIG_KEY_VERSION + '&signed_body=' + hmac.new(IG_SIG_KEY.encode('utf-8'),
                                                                                data.encode('utf-8'),
                                                                                hashlib.sha256).hexdigest() + '.' \
           + urllib.parse.quote_plus(data)


def generate_headers():
    return {
        "X-Pigeon-Session-Id": "3168f276-8c96-4db3-87af-1db1aa9cad09",
        "X-Pigeon-Rawclienttime": "1562978852"".860",
        "X-IG-Connection-Speed": "-1kbps",
        "X-IG-Bandwidth-Speed-KBPS": "-1.000",
        "X-IG-Bandwidth-TotalBytes-B": "0",
        "X-IG-Bandwidth-TotalTime-MS": "0",
        "X-Bloks-Version-Id": "c7aeefd59aab78fc0a703ea060ffb631e005e2b3948efb9d73ee6a346c446bf3",
        "X-IG-Connection-Type": "WIFI",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-App-ID": "567067343352427",
        "User-Agent": generate_user_agent(),
        "Accept-Language": "en-US",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",

        "X-FB-HTTP-Engine": "Liger",
        "Connection": "close"
    }  # This is very basic headers and is literally
    # copy pasted from burp. TODO replace this with headers that is randomly generated


def generate_user_agent():
    return "Instagram 101.0.0.15.120 Android (26/8.0.0; 320dpi; 768x1184; Genymotion/Android; " \
           "instagram_following_itsmoji; vbox86p; vbox86; en_US; 162439045) "  # TODO Generate random user agent


class Instagram(BaseSocialApp):

    def __init__(self, phone_numbers):
        self.last_response = None
        self.current_session = None
        super().__init__(phone_numbers)

    def authenticate(self):
        pass

    def setup_session(self):
        if self.current_session is not None:
            return

        self.current_session = requests.Session()
        self.current_session.headers.update({'Connection': 'close',
                                             'Accept': '*/*',
                                             'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                             'Cookie2': '$Version=1',
                                             'Accept-Language': 'en-US',
                                             'User-Agent': generate_user_agent()})

    def generate_data(self, phone_number_raw):
        data = {'phone_id': generate_uuid(True),
                'guid': generate_uuid(True),
                'device_id': generate_device_id(),
                'login_attempt_count': '0',
                'directly_sign_in': 'true',
                'source': 'default',
                'q': phone_number_raw,
                'ig_sig_key_version': SIG_KEY_VERSION
                }
        return data

    def detect_single_number(self, phone_number):
        self.setup_session()
        data = self.generate_data(phone_number.get_phone_number())

        response = self.current_session.post(USERS_LOOKUP_URL, data=generate_signature(json.dumps(data)))
        self.last_response = response
        if response.ok:
            phone_number.set_app_state(self.get_name(), PhoneNumber.AppUsageEnum.USAGE)
            # Check if the user has whatsapp too
            if response.json()['can_wa_reset']:
                phone_number.set_app_state("Whatsapp", PhoneNumber.AppUsageEnum.USAGE)  # TODO replace the hardcoded
                # whatsapp string with a centralized strings file
            else:
                phone_number.set_app_state("Whatsapp", PhoneNumber.AppUsageEnum.NO_USAGE)
        elif response.status_code == 404:
            phone_number.set_app_state(self.get_name(), PhoneNumber.AppUsageEnum.NO_USAGE)

    def detect_numbers(self, phone_numbers):
        for phone in phone_numbers:
            self.detect_single_number(phone)

    def process(self):
        # Making too many requests to Instagram will get the IP eventually blacklisted. You will need to invest in
        # private proxies If you do so, you should implement them in this function
        self.detect_numbers(self.phone_numbers_to_detect)

    def get_name(self):
        return "Instagram"
