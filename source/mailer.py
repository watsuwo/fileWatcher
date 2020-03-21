from email.mime.text import MIMEText
from email.utils import formatdate

import smtplib
import ssl

FROM_ADDRESS = 'hogehoge@gmail.com'
MY_PASSWORD = 'password'
TO_ADDRESS = 'receiver@example.com'
SUBJECT = 'TEST'
BODY = 'TESTメール'

def create_message(from_addr, to_addr, subject, body):
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = from_addr
    message['TO'] = to_addr
    message['Date'] = formatdate()
    return message

def send(from_addr, to_addrs, message):
    #context = ssl.create_default_context()
    smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, message.as_string())
    smtpobj.close()

def send_mail():
    message = create_message(FROM_ADDRESS, TO_ADDRESS, SUBJECT, BODY)
    send(FROM_ADDRESS, TO_ADDRESS, message)