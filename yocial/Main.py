# TODO Write unit tests
# TODO Write documentation

# Ultimately, I want Main.py to only have command arguments processing. Will work on that later
# Right now Main.py is used to demonstrate how to use the API
import sys
import yocial.Utils as Utils
import private_constants
from yocial.features.Instagram.Instagram import Instagram
from yocial.features.SocialDetector import SocialDetector
from yocial.features.Telegram.Telegram import Telegram
from yocial.features.Whatsapp.Whatsapp import Whatsapp


def main():
    phone_number_list = Utils.cmd_args_to_phone_number(sys.argv)
    detector = SocialDetector()
    detector.add_social_app(Telegram(phone_number_list, private_constants.TELEGRAM_API_ID, private_constants.TELEGRAM_API_HASH))
    detector.add_social_app(Whatsapp(phone_number_list))
    detector.add_social_app(Instagram(phone_number_list))
    detector.detect()
    for number in phone_number_list:
        print(number)


if __name__ == "__main__":
    main()
