import validators

all_host_data = [[],['10.222.2.2', 'Unavailable by ICMP ping', '0.0008%', '99.9992%', 'Show'],['1_Floor_2', 'Unavailable by ICMP ping', '0.0008%', '99.9992%', 'Show'], ['ADM_Floor_2', 'Unavailable by ICMP ping', '1.9498%', '98.0502%', 'Show'], ['ADM_FLoor_3', 'Unavailable by ICMP ping', '1.4352%', '98.5648%', 'Show'], ['A_Floor_4_1', 'Unavailable by ICMP ping', '2.2083%', '97.7917%', 'Show'], ['A_Floor_4_2', 'Unavailable by ICMP ping', '2.2199%', '97.7801%', 'Show'], ['A_Test', 'Unavailable by ICMP ping', '100.0000%', '', 'Show'], ['B_Design_Center', 'Unavailable by ICMP ping', '', '100.0000%', 'Show'], ['B_Floor_1', 'Unavailable by ICMP ping', '0.0023%', '99.9977%', 'Show'], ['B_Floor_2', 'Unavailable by ICMP ping', '0.0023%', '99.9977%', 'Show'], ['B_Floor_4', 'Unavailable by ICMP ping', '2.2206%', '97.7794%', 'Show'], ['D1_Floor_4', 'Unavailable by ICMP ping', '', '100.0000%', 'Show'], ['D1_Floor_5_512 Kartashev', 'Unavailable by ICMP ping', '0.0008%', '99.9992%', 'Show'], ['D1_Floor_5_512 Stend', 'Unavailable by ICMP ping', '0.0008%', '99.9992%', 'Show'], ['D1_Floor_5_Kartashev', 'Unavailable by ICMP ping', '0.0008%', '99.9992%', 'Show'], ['D1_Floor_6', 'Unavailable by ICMP ping', '', '100.0000%', 'Show'], ['D2_Floor_2', 'Unavailable by ICMP ping', '1.4452%', '98.5548%', 'Show'], ['D2_Floor_3', 'Unavailable by ICMP ping', '1.4452%', '98.5548%', 'Show'], ['D2_Floor_4', 'Unavailable by ICMP ping', '1.4452%', '98.5548%', 'Show'], ['G_Floor_3', 'Unavailable by ICMP ping', '0.0008%', '99.9992%', 'Show'], ['G_Floor_4', 'Unavailable by ICMP ping', '0.0008%', '99.9992%', 'Show'], ['L_Floor_2', 'Unavailable by ICMP ping', '0.0016%', '99.9984%', 'Show'], ['MED_Floor_3', 'Unavailable by ICMP ping', '1.4475%', '98.5525%', 'Show'], ['O_Floor_3', 'Unavailable by ICMP ping', '1.4413%', '98.5587%', 'Show'], ['V_Floor_2', 'Unavailable by ICMP ping', '0.0023%', '99.9977%', 'Show'], ['V_Floor_3', 'Unavailable by ICMP ping', '2.2207%', '97.7793%', 'Show']]
list1 = ['10.222.2.2', 'Unavailable by ICMP ping', '0.0008%', '99.9992%', 'Show']
list2 = ['1_Floor_2', 'Unavailable by ICMP ping', '0.0008%', '99.9992%', 'Show']
#print(type(all_host_data))

#print(all_host_data)


def ip_test(list):
    for el in list:
        if validators.ipv4(el) is True:
            return True

print ("=============================")
#ip_test(list2)
print("==============================")


new_all_host_date = []
for host in all_host_data:
    print(host)
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












