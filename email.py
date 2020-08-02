import smtplib
def call_smtp():
	smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
	print(smtp_obj.ehlo())