import requests
from random import randint
from user_agent import generate_user_agent
header = {'User-Agent': generate_user_agent(),'Accept': '*/*','Accept-Language': 'en-US,en;q=0.5','Referer': 'https://mega.nz/','Content-Type': 'text/plain;charset=UTF-8','Origin': 'https://mega.nz','Connection': 'keep-alive'}
omail = "YOUR_EMAIL"
mail = '%s","v":2}]' %(omail)
data = '[{"a":"ere","m":"'+mail
ids = randint(100000000, 999999999)
url = f"https://g.api.mega.co.nz/cs?id=-{ids}&=&domain=meganz&v=2&lang=en"
x = requests.post(url, headers=header, data=data).text
#print(x)
if x == '[{"val":0,"2fa":0}]':
  print(f"{omail} ==> EXISTS IN MEGA")
else:
  print(f"{omail} ==> NOT EXISTS IN MEGA")
