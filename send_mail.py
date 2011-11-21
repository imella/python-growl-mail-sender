import smtplib
import Growl
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

gmail_user = 'YOUR_GMAIL_ADDRESS'
gmail_pwd = 'YOUR_GMAIL_PASSWORD'

def mail(to, subject, text):
	msg = MIMEMultipart()
	msg['From'] = gmail_user
	msg['To'] = to
	msg['Subject'] = subject
	msg.attach(MIMEText(text))

	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(gmail_user, gmail_pwd)
	server.sendmail(gmail_user, to, msg.as_string())
	server.close()
	gn = Growl.GrowlNotifier("SendMail", ["Mail sent"])
	gn.register()
	gn.notify("Mail sent","Mail sent", "Mail to " + to + " has been sent")


mail(gmail_user, "Hello!", "This is a hello message")
