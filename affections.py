from dotenv import load_dotenv
from datetime import datetime as dt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import random
import smtplib

load_dotenv()

username = os.getenv('username')
password = os.getenv('password')
recipient = os.getenv('recipient')


file = os.path.expanduser('~/Desktop/play_around/Projects/Affections/affections.txt')


def text_parser(file_):
    """processes the text file, deletes each quote after using and shuffles the remaining"""

    with open(file_, 'r') as f:
        lines = f.readlines()
        text = lines.pop(0).strip() #deletes after copying
        random.shuffle(lines)

        with open(file_, 'w+') as g:
            g.writelines(lines)

    return text


def send_mail(username_, password_, recipients, email):
    """ function that sends out our emails"""

    subject = 'Always and Forever <3'
    body = email

    message = MIMEMultipart()
    message['from'] = username_
    message['To'] = recipients
    message["Subject"] = subject
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:

        try:
            server.ehlo()
            server.starttls()  # establish a secure connection
            server.ehlo()

            # log onto server
            server.login(username_, password_)

            # Send email
            server.sendmail(username_,
                            recipients.split(','),
                            message.as_string())

        except smtplib.SMTPException as e:
            print(f'A SMTP errror "{e}" occured')

        else:
            print(f'Email Successfully sent @ {dt.today()}')



if __name__ == '__main__':

    email = text_parser(file)
    send_mail(username, password, recipient, email)
