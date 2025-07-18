from twilio.rest import Client

account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
from_whatsapp_number = 'whatsapp:+14155238886' 
to_whatsapp_number = 'whatsapp:+91xxxxxxxxxx'   

client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Hello, this is a test message from Python via WhatsApp using Twilio!',
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

print(f"Message sent! SID: {message.sid}")
