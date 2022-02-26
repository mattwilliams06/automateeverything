import yagmail
from decouple import config
import pandas as pd

sender = config('senderID',default='')
password = config('senderPass',default='')
receiver = config('receiver',default='')


df = pd.read_csv('contacts2.csv')

def generate_file(filename, content):
    with open(filename,'w') as f:
        f.write(str(content))

for index,row in df.iterrows():
    name = row['name']
    amount = row['amount']
    generate_file(f'{name}.txt',amount)
    subject = 'This is the subject'

    contents = [f'''
    Hello {name}, you must pay ${amount}. Bill is attached.
    ''',f'{name}.txt']
    yag = yagmail.SMTP(user=sender,password=password)
    yag.send(to=receiver,subject=subject,contents=contents)
    print('Email sent')