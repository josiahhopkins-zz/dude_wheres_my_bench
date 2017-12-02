from twilio.rest import Client
import os
#The number the notification will be sent from
account_sid = os.environ['tw_acc_api']
auth_token = os.environ['tw_auth_token']
twilio_number = "+12064296852"
destination_number = os.environ['number']
client = Client(account_sid, auth_token)

#Sends a notification saying that [machine] is open
#Accepts a String [machine]
def send():
    message = client.messages.create(
        to=destination_number,
        from_=twilio_number,
        body="The bench is now open!")
