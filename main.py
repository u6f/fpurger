token = input("[\033[1;32;40m>\033[1;37;40m] Insert Token ")
import requests, time
from time import sleep
from requests import get, delete
friends = 0
o = open('Friends.txt', 'a')
f = get("https://discord.com/api/v9/users/@me/relationships", headers={'Authorization': token}).json()
for i in range(len(f)):
	friends += 1
for i in range(len(f)):
	o.write(f"\nf[i]['user']['id']")
	r = delete("https://discord.com/api/v9/users/@me/relationships/"+f[i]['user']['id'], headers={'Authorization': token})
	friends -= 1
	print(f"{r.status_code} | {f[i]['user']['id']} | {friends}")
	sleep(5)
