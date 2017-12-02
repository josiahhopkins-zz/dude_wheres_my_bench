from twilio.rest import Client
#The number the notification will be sent from
twilio_number = "+12064296852"

#Sends SMS messages
class Messenger:
    #The number the notification will be sent to. Currently fixed for prototyping
    #Evan's #
    destination_number = "+12535792510"
    #Connor's #
    #destination_number = "+12532821606"
    client = Client(account_sid, auth_token)

    #Sends a notification saying that [machine] is open
    #Accepts a String [machine]
    def send(self, machine):
        message = self.client.messages.create(
            to=self.destination_number,
            from_=twilio_number,
            body="The " + str(machine) + " is now open!")

#Test loop
#m = Messenger()
#m.send("Benchpress")
