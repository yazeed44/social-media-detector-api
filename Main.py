# TODO Write unit tests
# TODO Write documentation
# Ultimately, I want Main.py to only have command arguments processing. Will work on that later
# Right now Main.py is used to demonstrate how to use the API
import sys

import Utils
import private_constants
from Instagram import Instagram
from SocialDetector import SocialDetector
from Telegram import Telegram
from Whatsapp import Whatsapp


def main():
    phone_number_list = Utils.cmd_args_to_phone_number(sys.argv)
    detector = SocialDetector()
    # detector.add_social_app(Telegram(phone_number_list, private_constants.TELEGRAM_API_ID, private_constants.TELEGRAM_API_HASH))

    detector.add_social_app(Instagram(phone_number_list))
    detector.detect()
    for number in phone_number_list:
        print(number)


if __name__ == "__main__":
    main()
