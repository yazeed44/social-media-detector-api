class PhoneNumber:
    phone_number = ""
    has_telegram = False

    def __init__(self, phone_number):
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number

    def set_telegram(self, has_telegram):
        self.has_telegram = has_telegram

    def has_telegram(self):
        return self.has_telegram

    def __str__(self):
        return self.phone_number + ", Telegram: " + str(self.has_telegram)
