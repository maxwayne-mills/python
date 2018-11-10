#!/usr/bin/env python

from twilio.rest import client

account_sid = "Twilio account ID"
auth_token = "Twilio auth token"
from_number = "+16477928621"
to_number = "4166253512"

client = Client(account_sid, auth_token)

message = client.messages.create(
   to="to_number",
   from="from_number",
   body="Hello from oss")

print(message.sid)
