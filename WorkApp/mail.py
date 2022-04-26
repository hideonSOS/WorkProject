from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from importlib.resources import path
import smtplib
from os.path import basename
import os
from email.mime.image import MIMEImage
from email import encoders
#^^^^^^^^^^^^^^^^^^^^^
EMAIL_HOST="smtp.gmail.com"
EMAIL_HOST_USER="yamato.media.robots@gmail.com"
EMAIL_HOST_PASSWORD="dwabvwpqknziiauh"
EMAIL_PORT=587
EMAIL_USE_TLS=True
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# SMTP認証情報
account = "yamato.media.robots@gmail.com"
password = "yamato2020"


def send_image(subjecton,messageon,path,to_email):
	msg = MIMEMultipart()
	msg["Subject"] = subjecton
	msg["To"] = to_email
	msg["From"] = account
	msg.attach(MIMEText(messageon))
	
	for i in path:
		f= open(i.name,'wb+')
		# f= open(i.name,'w+')
		for chunk in i.chunks():
			f.write(chunk)
		f.close
		#--------------------------------------------
		f=open(i.name, 'rb')
		img = f.read()
		image = MIMEImage(img, name=i.name,_subtype='octet-stream')
		
		# image=MIMEText(img)
		msg.attach(image)
		f.close
		

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(account, EMAIL_HOST_PASSWORD)
	server.send_message(msg)
	server.quit()

import PyPDF2
def send_pdf(subjecton,messageon,path,to_email):
	msg=MIMEMultipart()
	msg['Subject']=subjecton
	msg["To"] = to_email
	msg["From"] = account
	msg.attach(MIMEText(messageon))
	
	for i in path:
		pdf=PyPDF2.PdfFileMerger()
		for i in path:
			pdf.append(i)
		pdf.write(str(i.name))
		pdf.close
		#--------------------------------------------
		f=open(i.name, 'rb')
		img = f.read()
		image = MIMEImage(img, name=i.name,_subtype='octet-stream')
		
		# image=MIMEText(img)
		msg.attach(image)
		f.close
		

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(account, EMAIL_HOST_PASSWORD)
	server.send_message(msg)
	server.quit()