from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from importlib.resources import path
import smtplib
from os.path import basename
import os

#^^^^^^^^^^^^^^^^^^^^^
EMAIL_HOST="smtp.gmail.com"
EMAIL_HOST_USER="yamato.media.robots@gmail.com"
EMAIL_HOST_PASSWORD="dwabvwpqknziiauh"
EMAIL_PORT=587
EMAIL_USE_TLS=True
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

to_email = "code1555@icloud.com"
# SMTP認証情報
account = "yamato.media.robots@gmail.com"
password = "yamato2020"


def send_mail(subjecton,messageon,path):
	msg = MIMEMultipart()
	msg["Subject"] = subjecton
	msg["To"] = to_email
	msg["From"] = account
	msg.attach(MIMEText(messageon))

	for i in path:
		f= open(i.name,'wb+')
		for chunk in i.chunks():
			f.write(chunk)
			part = MIMEApplication(f.read())
			msg.attach(part)
			f.close

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(account, EMAIL_HOST_PASSWORD)
	server.send_message(msg)
	server.quit()