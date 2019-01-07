#!/usr/bin/env python

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("clarence.mills@gmail.com")
to_email = Email("cmills@opensitesolutions.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", """and easy to do anywhere, even with Python. An invalid email occurs when you attempt to send email to an address that is formatted in a manner that does not meet internet email format standards. Examples include addresses without the @sign or addresses that include certain special characters and/or spaces.
""")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())

print(response.status_code)
print(response.body)
print(response.headers)