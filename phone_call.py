from twilio.rest import Client

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_number = '+1234567890'      
receiver_number = '+91xxxxxxxxxx'  

client = Client(account_sid, auth_token)

call = client.calls.create(
    to=receiver_number,
    from_=twilio_number,
    url='http://demo.twilio.com/docs/voice.xml'
)

print(f"Call initiated, SID: {call.sid}")
