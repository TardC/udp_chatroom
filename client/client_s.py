# coding: utf-8
from socket import *


def init():
    client_s_name = gethostname()
    client_s_ip = gethostbyname(client_s_name)
    client_s_port = 8887
    client_s_address = (client_s_ip, client_s_port)

    client_s = socket(AF_INET, SOCK_DGRAM)
    client_s.bind(client_s_address)

    return client_s


def main():
    client_s = init()
    server_ip = '192.168.131.1'
    server_port = 8888
    server_address = (server_ip, server_port)

    client_s.sendto('Usr', server_address)

    while True:
        data, address = client_s.recvfrom(2048)
        print data


if __name__ == '__main__':
    main()