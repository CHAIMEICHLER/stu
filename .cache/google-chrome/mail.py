import smtplib
from email.mime.multipart import MIMEMultipart


msg = MIMEMultipart()
msg['Subject'] = 'בדיקה מתוך פייתון'
msg['From'] = 'ca0527619864@gmail.com'
msg['To'] = 'ca0527619864@gmail.com'

string = 'abc'

s = smtplib.SMTP("smtp.gmail.com", 587)
s.ehlo()
s.starttls()
s.login("ca0527619864@gmail.com", 0527619864'pass')
s.sendmail("ca0527619864@gmail.com", 0527619864"@gmail.com", string)
s.quit()