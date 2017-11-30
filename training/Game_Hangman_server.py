import random
import socketserver

HOST = 'localhost'
PORT = 9999


class Hangman(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).decode()

        print('Клиент {} сообщает: {}'.format(self.client_address, self.data))

        x = random.randint(1, 100)

server = socketserver.TCPServer((HOST, PORT), Hangman)

print('Сервер игры "Виселица" запущен')

server.serve_forever()