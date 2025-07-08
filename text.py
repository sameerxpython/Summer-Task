from twilio.rest import Client

# Twilio credentials (Get these from https://www.twilio.com/console)
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_number = '+1234567890'  # Your Twilio phone number
receiver_number = '+91xxxxxxxxxx'  # Replace with the recipient's number

client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hello! This is a message sent from Python using Twilio.',
    from_=twilio_number,
    to=receiver_number
)

print(f"Message sent! SID: {message.sid}")
