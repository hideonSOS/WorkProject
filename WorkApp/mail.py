from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from importlib.resources import path
import smtplib
from os.path import basename
import os


# 送受信先
to_email = "code1555@icloud.com"



def send_mail(subjecton,messageon,path):
	# SMTP認証情報
	account = "yamato.media.robots@gmail.com"
	password = "yamato2020"
	msg = MIMEMultipart()
	msg["Subject"] = subjecton
	msg["To"] = to_email
	msg["From"] = "yamato.media.robots@gmail.com"
	msg.attach(MIMEText(messageon))

	for i in path:
		with open(i , "rb") as f:
			part = MIMEApplication(f.read(),Name=basename(i))
			part['Content-Disposition'] = 'attachment; filename="%s"' % basename(i)
			msg.attach(part)
	# メール送信処理
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(account, password)
	server.send_message(msg)
	server.quit()