import yagmail
import time
from datetime import datetime as dt
from decouple import config

sender = config('senderID',default='')
password = config('senderPass',default='')
receiver = config('receiver',default='')

subject = 'This is the subject'

contents = '''
Here is the content of the email.
'''

while True:
    now = dt.now()
    if now.hour == 12 and now.minute == 34:
        yag = yagmail.SMTP(user=sender,password=password)
        yag.send(to=receiver,subject=subject,contents=contents)
        print('Email sent')
        time.sleep(60)