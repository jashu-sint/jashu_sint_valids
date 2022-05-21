import requests
from fake_useragent import UserAgent
import json

ua = UserAgent()
email= "YOUR_EMAIL"
headers = {
'User-Agent': str(ua.random)}
a = requests.get(f"https://api.twitter.com/i/users/email_available.json?email={email}", headers=headers).json()
if a["taken"] == True:
   print(f"{email} ==> exist in TWITTER")
else:
  print(f"{email} ==> Not exist in TWITTER")
