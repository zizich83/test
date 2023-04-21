import requests
import fake_useragent
import re
import validators
import jinja2_template
from bs4 import BeautifulSoup


session = requests.Session()
def ip_test(list):
    for el in list:
        if validators.ipv4(el) is True:
            return True

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
report_info = "http://zabbix.inet.eprib.ru/zabbix/report2.php?mode=1&from=now-3M&to=now&filter_groupid=9&filter_templateid=10552&tpl_triggerid=23057&hostgroupid=0&filter_set=1"
#report_info = "http://zabbix.inet.eprib.ru/zabbix/report2.php?mode=1&from=now-3h&to=now&filter_groupid=9&filter_templateid=10552&tpl_triggerid=23058&hostgroupid=0&filter_set=1&filter_set=1"
report_response = session.get(report_info).text
#print(report_response)



cookies_dict = [
	{"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
	for key in session.cookies
]

session2 = requests.Session()
for cookies in cookies_dict:
	session2.cookies.set(**cookies)

response2 = session2.get(report_info, headers=header).text
soup = BeautifulSoup(response2, 'lxml')
block = soup.find('table', class_="list-table")
all_hosts = block.find_all('tr')
all_host_data = []
for host in all_hosts:
	host_data = host.find_all('td')
	result= []
	#print("===NEW-ELEMEMT===")
	host_list = []
	for el_host_data in host_data:
		el_host_data = str(el_host_data)
		el_host_data = re.sub(r'\<[^<>]*\>', '', el_host_data)
		host_list.append(el_host_data)
		#print(host_list)

	all_host_data.append(host_list)
print(all_host_data)
new_all_host_date = []
for host in all_host_data:
    #print(host)
    if len(host) == 0:
        print("empty")
        continue
    elif ip_test(host) is True:
        continue
    else:
        del host[-1]
        del host[1]
    new_all_host_date.append(host)
print(new_all_host_date)

jinja2_template.template_html_report(new_all_host_date)




print("===========================")

with open("zabbix.html", "w", encoding="utf-8") as file:
    file.write(block.text)








# Session
# Authorization
# Get/Set cookies

# http://zabbix.elprib.ru/
# Admin:BARhfrelf7