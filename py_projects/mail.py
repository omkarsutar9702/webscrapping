import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_mail(filename):
    from_add = 'your email id from to send'
    to_add = 'your email id to send'
    subject = 'stock information of Amazon, google , telsa , colgate'

    msg = MIMEMultipart()
    msg['from'] = from_add
    msg['to'] = to_add
    msg['subject'] = subject

    body="here you can find the csv file"
    msg.attach(MIMEText(body,'plain'))

    my_file = open(filename,'rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload(my_file.read())


    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment ; filename='+filename)
    msg.attach(part)

    massage=msg.as_string()


    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(from_add,'iigqxwclffiwjhxh')
    server.sendmail(from_add,to_add,massage)
    server.quit()