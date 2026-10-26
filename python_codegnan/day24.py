# import smtplib
# sender='kondrunagasudha08@gmail.com'
# password='iyjg zcpa chfn djes'
# receiver='wd.rkad@gmail.com'
# message='Hi sir'
# with smtplib.SMTP('smtp.gmail.com',587) as conn:
#     conn.starttls()
#     conn.login(sender,password)
#     conn.sendmail(sender,receiver,message)
# print('email sent successfully')

import smtplib
from email.message import EmailMessage
sender='kondrunagasudha08@gmail.com'
password='iyjg zcpa chfn djes'
receiver='wd.rkad@gmail.com'
# message='Hi sir'
msg_obj = EmailMessage()
msg_obj['From'] = "kondrunagasudha08@gmail.com"
msg_obj['To'] = "wd.rkad@gmail.com"
msg_obj['Subject'] = "Test"
msg_obj.set_content("Hello from Python!")
filename='nature.jpg'
# for filename in filenames:  when multiple files are given or attached
with open(filename, 'rb') as file:
    data = file.read()
    msg_obj.add_attachment(data, maintype='application', subtype='octet-stream', filename=filename)
with smtplib.SMTP('smtp.gmail.com',587) as conn:
    conn.starttls()
    conn.login(sender,password)
    conn.send_message(msg_obj)
print("Email sent!")