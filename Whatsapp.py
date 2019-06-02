from BaseSocialApp import BaseSocialApp
import subprocess


class Whatsapp(BaseSocialApp):
    def authenticate(self):
        # TODO implement a robust way to verify through qr code
        # Currently, Whatsapp go will try to verify through qr code and will time out if not entered within a minute
        pass

    def detect_single_number(self, phone_number):
        self.detect_numbers([phone_number])

    def detect_numbers(self, phone_numbers):
        # The first time whatsapp_detect.go is used will require a qr code scan.
        command = 'go run whatsapp_detect.go'
        for phone in phone_numbers:
            command = command + " " + phone.get_phone_number()
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        result_decoded = output.stdout.decode('utf-8').splitlines()
        for index, phone in enumerate(phone_numbers):
            # For each phone number, look for the corresponding line in the output
            phone.set_whatsapp("\"status\":200" in result_decoded[index])
        return phone_numbers
