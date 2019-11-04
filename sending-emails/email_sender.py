import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Evelyn Le'
email['to'] = 'evelynle2019@gmail.com'
email['subject'] = 'Hello from PyCharm!'

email.set_content(html.substitute({'name': "TinTin"}), "html")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('evelynle1024@gmail.com', 'ilovecoding@1')
    smtp.send_message(email)
    print('All done!')
