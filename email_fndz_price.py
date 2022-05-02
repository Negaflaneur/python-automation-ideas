import smtplib
import os
from email.message import EmailMessage
import time, datetime
import requests, json
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
request = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=fndz-token&vs_currencies=usd')
json_file = json.loads(request.text)
fndz_price_msg = f'Current FNDZ price is {json_file["fndz-token"]["usd"]}'

email = smtplib.SMTP('smtp.gmail.com', 587)
email_address = 'example@gmail.com'
email_pass = os.environ.get('email_test_pass')
email.ehlo()
email.starttls()
email.ehlo()
email.login(email_address, f'{email_pass}')

email_message = EmailMessage()
email_message['From'] = email_address
email_message['To'] = email_address
email_message['Subject'] = 'FNDZ price update'
email_message.set_content(fndz_price_msg)

email.send_message(email_message)
print("Email sent")
email.quit()


