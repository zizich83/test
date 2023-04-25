import csv
switches_info = "http://zabbix.inet.eprib.ru/zabbix/report2.php?mode=1&from=now-3M&to=now&filter_groupid=9&filter_templateid=10552&tpl_triggerid=23057&hostgroupid=0&filter_set=1"
servers_report = "http://zabbix.inet.eprib.ru/zabbix/report2.php?mode=1&from=now-3M&to=now&filter_groupid=10&filter_templateid=10580&tpl_triggerid=24976&hostgroupid=0&filter_set=1"

reports_info = {
    'servers_report' : "http://zabbix.inet.eprib.ru/zabbix/report2.php?mode=1&from=now-3M&to=now&filter_groupid=10&filter_templateid=10580&tpl_triggerid=24976&hostgroupid=0&filter_set=1",
    'switches_report' : "http://zabbix.inet.eprib.ru/zabbix/report2.php?mode=1&from=now-3M&to=now&filter_groupid=10&filter_templateid=10580&tpl_triggerid=24976&hostgroupid=0&filter_set=1"
}

for key,value in reports_info.items():
    print(key)
    print(value)

cols = [ 'Hostname', 'Problems', 'ok']
rows = [['1_Floor_2', '0.0015%', '99.9985%'], ['ADM_Floor_2', '1.9498%', '98.0502%'], ['ADM_FLoor_3', '1.4352%', '98.5648%'], ['A_Floor_4_1', '2.2083%', '97.7917%'], ['A_Floor_4_2', '2.2199%', '97.7801%'], ['A_Test', '100.0000%', ''], ['B_Design_Center', '', '100.0000%'], ['B_Floor_1', '0.0023%', '99.9977%'], ['B_Floor_2', '0.0031%', '99.9969%'], ['B_Floor_4', '2.2214%', '97.7786%'], ['D1_Floor_4', '', '100.0000%'], ['D1_Floor_5_512 Kartashev', '0.0008%', '99.9992%'], ['D1_Floor_5_512 Stend', '0.0015%', '99.9985%'], ['D1_Floor_5_Kartashev', '0.0008%', '99.9992%'], ['D1_Floor_6', '', '100.0000%'], ['D2_Floor_2', '1.4452%', '98.5548%'], ['D2_Floor_3', '1.4452%', '98.5548%'], ['D2_Floor_4', '1.4452%', '98.5548%'], ['G_Floor_3', '0.0008%', '99.9992%'], ['G_Floor_4', '0.0015%', '99.9985%'], ['L_Floor_2', '0.0016%', '99.9984%'], ['MED_Floor_3', '1.4475%', '98.5525%'], ['O_Floor_3', '1.4413%', '98.5587%'], ['V_Floor_2', '0.0023%', '99.9977%'], ['V_Floor_3', '2.2215%', '97.7785%']]
with open('show.csv' , 'w') as f:
    write = csv.writer((f))
    write.writerow(cols)
    write.writerows(rows)