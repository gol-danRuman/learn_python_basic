SENDGRID_API_KEY='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'


# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='ruman@fusemachines.com',
    to_emails='rumancha12@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)