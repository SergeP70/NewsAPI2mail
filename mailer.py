# install SSL certificate when SSL-error
# install pip python-dotenv
# /Applications/Python/3.12/Install/Certificates.command with admin privileges
import smtplib
import ssl
from email.message import EmailMessage
# import environment variables:
import os
from dotenv import load_dotenv
load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
my_context = ssl.create_default_context()


def send(receiver, subject, message):
    mail = EmailMessage()
    mail['From'] = username
    mail['To'] = receiver
    mail['Subject'] = subject
    message = message + "\n This is a message from: " + receiver
    mail.set_content(message)

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.send_message(mail)
        server.quit()

