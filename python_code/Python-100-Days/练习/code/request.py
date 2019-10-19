import requests

url = 'https://live.kuaishou.com/u/3x3hxqujua4ad2g/3x7vr7jg' \
      'h2ctytm?did=web_ec667c' \
      '168a134840a9f46c866' \
      '31ad7ef'

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
re = requests.get(url, headers=headers)
with open("kuaishou.html","w",encoding="utf-8") as f:
    f.write(re.text)
