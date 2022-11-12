"""Module docs"""

# import
import sys
from yaml import full_load, YAMLError
from yocial import app_utils
from yocial.features.Instagram.Instagram import Instagram
from yocial.features.SocialDetector import SocialDetector
from yocial.features.Telegram.Telegram import Telegram
from yocial.features.Whatsapp.Whatsapp import Whatsapp


def get_secret() -> dict:
    """ get telegram secret keys from yml file """
    with open("yocial/config.yml", 'r', encoding="utf-8") as stream:
        try:
            return full_load(stream)['telegram'].values()
        except YAMLError as exception:
            raise exception


def main():
    '''docs'''
    phone_number_list = app_utils.cmd_args_to_phone_number(sys.argv)
    detector = SocialDetector()
    secret_id, secret_hash = get_secret()
    # detector.add_social_app(
    #    Telegram(
    #        phone_number_list,
    #        secret_id,
    #        secret_hash,
    #    )
    # )
    # detector.add_social_app(Whatsapp(phone_number_list))
    detector.add_social_app(Instagram(phone_number_list))
    detector.detect()
    for number in phone_number_list:
        print(number)


if __name__ == "__main__":
    main()
