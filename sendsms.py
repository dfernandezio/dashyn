from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "[YOUR TWILIO ACCOUNT ID]"
auth_token  = "[YOUR TWILIO TOKEN]"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Dashyn Alert Triggered",
    to="+10000000000",    # Replace with desired recipient phone number
    from_="+11111111111") # Replace with your Twilio Account Phone Number
print message.sid
