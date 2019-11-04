from twilio.rest import Client

account_sid = 'AC059026849476180aa487cddf897e0d87'
auth_token = '9ff9e8c20231ea62c12f2a9201cde866'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12019037715',
    body='I am using Twilio API. It is working!',
    to='+14843931759'
)

print(message.sid)