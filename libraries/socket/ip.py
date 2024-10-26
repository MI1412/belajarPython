import socket
import requests
import pprint
import json

# ping
host = input("masukkan domain: ")
ip_addres = socket.gethostbyname(host)

print(f"domain {host}\nip: {ip_addres}")

# requests url
request_url = 'https://geolocation-db.com/jsonp' + ip_addres
response = requests.get(request_url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)
print(geolocation)

for k,v in geolocation.items():
    print(k,v)