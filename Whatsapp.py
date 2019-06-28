from BaseSocialApp import BaseSocialApp
import subprocess
import os.path


class Whatsapp(BaseSocialApp):

    def authenticate(self):
        # Currently, Whatsapp go will try to verify through qr code and will time out if not entered within a minute
        # command = 'go run whatsapp_detect.go auth'
        # output = subprocess.run(command, shell=True)
        # print(output)
        # TODO implement a way to have multiple whatsapp sessions
        if not os.path.isfile("whatsappSession.gob"):
            print("Whatsapp will need authorization to your account. Scan the shown qr code. You might need to "
                  "restart the program after scanning the qr code")

            subprocess.run('go run whatsapp_detect.go auth', shell=True)

    def detect_single_number(self, phone_number):
        self.detect_numbers([phone_number])

    def detect_numbers(self, phone_numbers):
        # The first time whatsapp_detect.go is used will require a qr code scan.
        # TODO fix a potential bug where the result of the commands will not match the length of phone numbers' length
        self.authenticate()
        command = 'go run whatsapp_detect.go'
        for phone in phone_numbers:
            command = command + " " + phone.get_phone_number()
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        result_decoded = output.stdout.decode('utf-8').splitlines()
        for index, phone in enumerate(phone_numbers):
            # For each phone number, look for the corresponding line in the output
            phone.set_whatsapp("\"status\":200" in result_decoded[index])
        return phone_numbers

    def process(self, phone_numbers):
        # TODO implement an optimal algorithem for whatsapp where various client phone numbers are used to detect
        self.detect_numbers(phone_numbers)
