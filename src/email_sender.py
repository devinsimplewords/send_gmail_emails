import os
import smtplib
import time
from email.mime.text import MIMEText

from dotenv import load_dotenv


class EmailSender:

    def __init__(self):
        # load env variables
        load_dotenv()

        # get email and password from environment variables
        self.sender = os.getenv('SENDER_ADDRESS')
        self.password = os.getenv('SENDER_PASSWORD')

        if not self.sender or not self.password:
            raise ValueError("Missing sender or password, please check .env file.")

        # do the login
        self.session = self.server_login()

    def server_login(self):
        """Do the login using credentials stored in environment variables"""
        print("Login...")
        session = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465)
        session.login(user=self.sender, password=self.password)

        return session

    def server_logout(self):
        """Do the logout"""
        print("Logout...")
        self.session.quit()

    def send_email(self, email_info_list):
        """For each row present in the CSV file, send an email.
        When all the emails have been processed, do the logout.
        """
        for email_info in email_info_list:
            target_email = email_info[0]
            email_text = email_info[1]
            email_subject = email_info[2]

            msg = MIMEText(email_text, "html")
            msg["Subject"] = email_subject
            msg["From"] = self.sender
            msg["To"] = target_email

            self.session.sendmail(self.sender, target_email, msg.as_string())

            print("Email sent to {}".format(target_email))

            time.sleep(1)

        self.server_logout()
