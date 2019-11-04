from twilio.rest import Client

account_sid = '####'
auth_token = '###'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='###',
    body='I am using Twilio API. It is working!',
    to='my number'
)

print(message.sid)