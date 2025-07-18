from twilio.rest import Client

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_number = '+1234567890'  
receiver_number = '+91xxxxxxxxxx' 

client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hello! This is a message sent from Python using Twilio.',
    from_=twilio_number,
    to=receiver_number
)

print(f"Message sent! SID: {message.sid}")
