from dotenv import load_dotenv
from datetime import datetime as dt
import os
import smtplib

load_dotenv()

username = os.getenv('username')
password = os.getenv('password')
recipient = os.getenv('recipient')
file = os.path.expanduser('~/Desktop/play_around/affections.txt')



def text_parser(file_):
    """processes the text file"""

    pass


def send_mail(username_, password_, recipients, email):
    """ function that sends out our emails"""

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()  # establish a secure connection
    server.ehlo()

    # log onto server
    server.login(username_, password_)

    subject = 'Always and Forever <3'
    body = email
    message = f'Subject: {subject}\n\n{body}'
    recipients = recipients.split(',')

    # Send email
    server.sendmail(username_, recipients, message)
    print(f'Email Successfully sent @ {dt.today()}')

    # close connection
    server.quit()
    return recipients


if __name__ == '__main__':

    email = text_parser(file)
    send_mail(username, password, recipient, email)
