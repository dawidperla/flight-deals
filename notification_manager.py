from twilio.rest import Client

TWILIO_SID = "AC3de603666fdbf7f13a134fdc8cdfa1f8"
TWILIO_AUTH_TOKEN = "5e207d6c85e90ea73b72c665525797c8"
TWILIO_VIRTUAL_NUMBER = "+13192545649"
TWILIO_VERIFIED_NUMBER = "+48698117913"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
