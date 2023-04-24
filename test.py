switches_info = "http://zabbix.inet.eprib.ru/zabbix/report2.php?mode=1&from=now-3M&to=now&filter_groupid=9&filter_templateid=10552&tpl_triggerid=23057&hostgroupid=0&filter_set=1"
servers_report = "http://zabbix.inet.eprib.ru/zabbix/report2.php?mode=1&from=now-3M&to=now&filter_groupid=10&filter_templateid=10580&tpl_triggerid=24976&hostgroupid=0&filter_set=1"

reports_info = {
    'servers_report' : "http://zabbix.inet.eprib.ru/zabbix/report2.php?mode=1&from=now-3M&to=now&filter_groupid=10&filter_templateid=10580&tpl_triggerid=24976&hostgroupid=0&filter_set=1",
    'switches_report' : "http://zabbix.inet.eprib.ru/zabbix/report2.php?mode=1&from=now-3M&to=now&filter_groupid=10&filter_templateid=10580&tpl_triggerid=24976&hostgroupid=0&filter_set=1"
}

for key,value in reports_info.items():
    print(key)
    print(value)