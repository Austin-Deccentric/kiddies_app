import requests

url = 'http://127.0.0.1:5000/api/check'

with open('SFW.txt', 'rb') as f:
    r = requests.post(url, files={'story': f.read()})

#curl -X POST 'http://127.0.0.1:5000/api/check' -F 'story=@SFW.txt' -i
#CURL -F 'story=@SFW.txt' -X POST 'http://127.0.0.1:5000/api/check'
