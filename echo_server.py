#!/bin/env python3
import esockets
import logging, sys
import threading
root = logging.getLogger()
root.setLevel(logging.DEBUG)
fh = logging.FileHandler('spam.log')
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)
#
class MyClientHandler(esockets.ClientHandler):
    def handle_socket_message(self):
        message = self.recv(1024).strip()
        message = self.recv(1024).strip()
        print('Client: ', message)
        self.send(b'Server: ' + message + b'\n')
        return True

    def handle_socket_accept(self):
        print(self.address, ' Connected: ')
        return True

    def handle_socket_close(self, reason=''):
        self.send(b'Closing socket: ' + reason.encode() + b'\n')
        print(self.address, ' Disconnected: ', reason)

#
# # server = esockets.SocketServer(handle_incoming=handle_incoming,
# #                                handle_readable=handle_readable,
# #                                handle_closed=handle_closed)

port = int(sys.argv[1])
server = esockets.SocketServer(host='130.240.202.41', port=port, client_handler=MyClientHandler)
#
server.start()
# print('Server started on: {}:{}'.format(server.host, server.port))
#
# # server = esockets.SocketServer()
# # server.start()

# import socketserver
#
#
# clients = []
#
# class Client(socketserver.BaseRequestHandler):
#     def handle(self):
#         print(self.client_address, ' Connected')
#         clients.append(self.request)
#         return True
#
# HOST, PORT = "localhost", 9999
#
# # Create the server, binding to localhost on port 9999
# server = socketserver.TCPServer((HOST, PORT), Client)
# server.allow_reuse_address  = True
# server.serve_forever(2)

