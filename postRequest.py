import requests

url = 'https://customer-api.krea.se/coding-tests/api/squid-game'
myobj = {
    "answer": "21070",
    "name": "Larisa Darolti"
}
x = requests.post(url, json=myobj)

print(x.json())
