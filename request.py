import requests

url = 'http://127.0.0.1:5000/recommend'


payload = {"domain": "JS"}
r = requests.post(url, json=payload)
print(r.json())
