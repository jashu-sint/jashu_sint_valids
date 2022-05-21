import requests
from fake_useragent import UserAgent
import json

ua = UserAgent()

email = "YOUR_EMAIL"
p = {"source_url": "/",
"data": '{"options": {"email": "' + email + '"}, "context": {}}'}

headers = {
'User-Agent': str(ua.random)}
a = requests.get("https://www.pinterest.com/_ngjs/resource/EmailExistsResource/get/", headers=headers, params=p).json()
if "source_field" in str(a["resource_response"]["data"]):
   print(f"{email} ==> Not exist in PINTEREST")
elif a["resource_response"]["data"]:
   print(f"{email} ==> exist in PINTEREST")
else:
   print(f"{email} ==> Not exist in PINTEREST")
