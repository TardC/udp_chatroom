# coding: utf-8
from socket import *


def init():
    client_c_name = gethostname()
    client_c_ip = gethostbyname(client_c_name)
    client_c_port = 8886
    client_c_address = (client_c_ip, client_c_port)

    client_c = socket(AF_INET, SOCK_DGRAM)
    client_c.bind(client_c_address)

    return client_c


def main():
    client_c = init()
    server_ip = '192.168.131.1'
    server_port = 8888
    server_address = (server_ip, server_port)

    while True:
        message = raw_input("Message>> ")
        client_c.sendto(message, server_address)

        if message == '-q':
            break

    client_c.close()

if __name__ == '__main__':
    main()
