import datetime
import smtplib
from email.mime.text import MIMEText
import os

class Tools:
    def __init__(self,EMAIL_TO = "meier.thales@gmail.com"):
        self.EMAIL_TO = EMAIL_TO
        self.SMTP_SERVER = "smtp.gmail.com"
        self.SMTP_PORT = 587
        self.SMTP_USERNAME = "thalestmmpython@gmail.com"
        self.SMTP_PASSWORD = input("Type in the password: ")
        self.EMAIL_TO = "meier.thales@gmail.com"
        self.EMAIL_FROM = "Your Daily Update"
        self.EMAIL_SUBJECT = f"{datetime.date.today()} Update"
        self.filename = "message.txt"

    def create_global_file(self,comment = False):
        open(f"{self.filename}","w+")

        if comment:
            print("Raw Global file created")

    def send_email(self,type="html"):
        with open(self.filename,"r") as text_file:
            self.DATA = text_file.readlines()
            self.DATA = ''.join(self.DATA)
        msg = MIMEText(self.DATA,type)
        msg['Subject'] = self.EMAIL_SUBJECT
        msg['To'] = self.EMAIL_TO
        msg['From'] = self.EMAIL_FROM
        mail = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
        mail.starttls()
        mail.login(self.SMTP_USERNAME, self.SMTP_PASSWORD)
        mail.sendmail(self.EMAIL_FROM, self.EMAIL_TO, msg.as_string())
        mail.quit()
        os.remove(self.filename)
