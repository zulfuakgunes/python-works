import smtplib
import os
import imghdr
from email.message import EmailMessage
from collections import namedtuple
senderinfo = namedtuple('senderinfo', ('email', 'password'))
sender = senderinfo(os.environ.get('PYEMAIL'), os.environ.get('PYPASSWORD'))

mail = EmailMessage()
mail['Subject'] = 'This is subject'
mail['From'] = f'Sender Name <{sender.email}>'
mail['To'] = ['', '', '']  # Put the emails here as much as you wish. Seperate them with comma.
mail.add_alternative("""\
This mail sent by <b>{0}</b>
""".format(sender.email), subtype='html')  # Mail content using html

imgfiles = ['./images/img1.jpg', './images/img2.png']  # image files if you wish to add
for imgfile in imgfiles:
    with open(imgfile, 'rb') as file:
        file_data = file.read()
        file_type = imghdr.what(file.name)
        file_name = file.name.split('/')[-1]
    mail.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

pdfiles = ['./pdfs/pdf1.pdf', './pdfs/pdf2.pdf']  # pdf files if you wish to add
for pdfile in pdfiles:
    with open(pdfile, 'rb') as f:
        file_data = f.read()
        file_name = f.name.split('/')[-1]
    mail.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender.email, sender.password)
    smtp.send_message(mail)
    print(smtp.send_message(mail))
