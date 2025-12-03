#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Force UTF-8 for the entire process (works even on broken Windows cmd)
os.environ["PYTHONIOENCODING"] = "utf-8"

sender_email = input("SENDER EMAIL: ").strip()
receiver_email = input("RECEIVER EMAIL: ").strip()
subject = input("SUBJECT: ").strip()
message = input("MESSAGE: ").strip()   # you can type anything here now

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(message, "plain", "utf-8"))

password = input("PASSWORD: ").strip()

server = smtplib.SMTP("smtp.gmail.com", 587, local_hostname="localhost")
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, msg.as_bytes())
server.quit()

# Safe print that never raises UnicodeEncodeError
try:
    print(f"Email successfully sent to {receiver_email}")
except UnicodeEncodeError:
    print("Email successfully sent to", receiver_email.encode('utf-8', errors='replace').decode('cp437', errors='replace'))



#nwpz sfev prlg wftt (app password)
#python manage.py runserver 0.0.0.0:8000