from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_number = '+1234567890'      # Your Twilio phone number
receiver_number = '+91xxxxxxxxxx'  # Replace with the recipient's number

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Make the call
call = client.calls.create(
    to=receiver_number,
    from_=twilio_number,
    url='http://demo.twilio.com/docs/voice.xml'  # TwiML to dictate the call behavior
)

print(f"Call initiated, SID: {call.sid}")
