from email.message import EmailMessage
from login_details import email , password 


import smtplib
import ssl


email_sender = email
email_password = password

email_receiver = 'nirel28629@ulforex.com' #temporary mail_id

subject = 'Testing my script'
body = """
This is a test message to check whether my code working properly or not.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())