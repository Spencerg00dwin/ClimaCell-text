# Twillio Account ID = ACd9a6d92ebe769400b17e6e0f075ea967
# Twillio Auth Token = 900b1ab460c099deb68467e5d1400efb
  
# GOOD_MORNING_QUOTES = ["Good Morning Love!",
#                         "Shabba",
#                         "shooba",
#                         "libba dee dum"]


# from twilio.rest import Client
# import schedule
# import random

# cellphone = 123
# twilio_number = 234
# def send_message(quote):
#     account = "ACd9a6d92ebe769400b17e6e0f075ea967"
#     token = "900b1ab460c099deb68467e5d1400efb"
#     client = Client(account.token)

#     client.messages.create(to=cellphone,
#                             from =twilio_number,
#                             body=quote)
# quote = GOOD_MORNING_QUOTES[random.randint(0, len(GOOD_MORNING_QUOTES))]
# schedule.every().day.at("09:00").do(send_message, quote)

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACd9a6d92ebe769400b17e6e0f075ea967"
# Your Auth Token from twilio.com/console
auth_token  = "900b1ab460c099deb68467e5d1400efb"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17038690578", 
    from_="++19293482171",
    body="Hello from Python!")

print(message.sid)