import yagmail
from decouple import config
import pandas as pd

sender = config('senderID',default='')
password = config('senderPass',default='')
receiver = config('receiver',default='')

subject = 'This is the subject'

contents = ['''
Here is the content of the email.
''','text.txt']

yag = yagmail.SMTP(user=sender,password=password)
yag.send(to=receiver,subject=subject,contents=contents)
print('Email sent')