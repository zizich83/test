import requests
import fake_useragent
from bs4 import BeautifulSoup

session = requests.Session()

link = 'http://zabbix.inet.eprib.ru/zabbix/index.php'
data = {
	"name": "Admin",
	"password": "BARhfrelf7",
	"autologin": "1",
	"enter": "Sign+in"
}
user = fake_useragent.UserAgent().random

header = {'user-agent': user}


response = session.post(link, data, headers=header).text

profile_info = "http://zabbix.inet.eprib.ru/zabbix/zabbix.php?action=userprofile.edit"
profile_response = session.get(profile_info).text
print(profile_response)


cookies_dict = [
	{"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
	for key in session.cookies
]

session2 = requests.Session()
for cookies in cookies_dict:
	session2.cookies.set(**cookies)

response2 = session2.get(profile_info, headers=header)

print(response2)


with open("zabbix.html", "w", encoding="utf-8") as file:
    file.write(response2.text)








# Session
# Authorization
# Get/Set cookies

# http://zabbix.elprib.ru/
# Admin:BARhfrelf7