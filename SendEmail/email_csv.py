import yagmail
from decouple import config
import pandas as pd

sender = config('senderID',default='')
password = config('senderPass',default='')
receiver = config('receiver',default='')

subject = 'This is the subject'

df = pd.read_csv('contacts.csv')

for receiver,name in zip(df.email,df.name):
    contents = f'Hello {name}, this is the content of the email.'
    yag = yagmail.SMTP(user=sender,password=password)
    yag.send(to=receiver,subject=subject,contents=contents)
    print('Email sent')