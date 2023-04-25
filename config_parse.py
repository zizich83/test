# ~ Парсинг различных конфигурационных файлов
import re
import pprint
#Парсинг ini файлов
def parse_cfg(file):
    result = {}
    file = open(file)
    regex_key = (' *\[(?P<key>\S+)] *')
    regex_value = (' *(?P<key>\S+) *= *(?P<value>\S+) *')
    for line in file:
        match_key = re.match(regex_key,line)
        match_value = re.match(regex_value,line)
        if match_key:
            key_sec = match_key.group('key')
            result[key_sec] ={}
            result[key_sec][key_sec] = key_sec
        elif match_value:
            key_value = match_value.group('key')
            value = match_value.group('value')
            result[key_sec][key_value] = value
    return result

#cfg = parse_cfg('config.cfg')
#print(cfg)
#device_ip = cfg['Core'].get('device_ip')
#print(device_ip)


