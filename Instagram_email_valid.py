email="YOUR_EMAIL"
import requests
r = requests.Session()
url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
r.headers = {'user-agent': user_agent}
r.headers.update({'X-CSRFToken': "missing"})

data = {"email_or_username":email}
req = r.post(url, data=data)

if req.text.find(f"We sent an {email} to")>=0:
  print(f"{email} ==> exist in INSTA")
elif req.text.find("password")>=0:
  print(f"{email} ==> exist in INSTA")
elif req.text.find("sent")>=0:
  print(f"{email} ==> exist in INSTA")
else:
  print(f"{email} ==> Not exist in INSTA")
