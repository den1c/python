import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  # Создаем ARP запрос.Что узнать кто
    # имено использует этот ip адрес.
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')  # Создаем широковещательный адрес MAC АДРЕСОВ.
    arp_request_broadcast = broadcast / arp_request  # Обьединяем два пакета в один запрос.
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]  # Отправляем запрос.И получаем ответ.
    # Получаем два списка(отвечанные,неотвечанные)

    clients_list = []
    # Проходим через цикл элементы из полученого списка.
    for element in answered_list:
        client_dist = {'IP': element[1].psrc, 'MAC': element[1].hwsrc}  # Создаем словарь.
        clients_list.append(client_dist)

    return clients_list


def print_result(result_list):
    # Создаем шабку таблицы.
    print('______________________________________________________________\n'
          '\tIP\t\t\t\t\tMAC Address\n'
          '______________________________________________________________')
    for client in result_list:
        print(client['IP'] + '\t\t\t' + client['MAC'])


scan_result = scan('192.168.0.1/24')
print_result(scan_result)
