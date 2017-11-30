import socket

HOST = 'localhost'
PORT = 9999

print('Клиент игры "Виселица" приветствует вас!')
print('Подключение к серверу {}:{}'.format(HOST, PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

sock.sendall(bytes('START', 'utf-8'))

sock.close()