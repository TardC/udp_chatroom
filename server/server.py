# coding: utf-8
from socket import *


def init():  # 创建套接字
    server_name = gethostname()
    server_ip = gethostbyname(server_name)
    server_port = 8888
    server_address = (server_ip, server_port)

    server = socket(AF_INET, SOCK_DGRAM)
    server.bind(server_address)

    return server


def main():
    addresses = []  # 记录客户端信息
    server = init()

    while True:
        data, address = server.recvfrom(2048)

        if data.startswith('Usr') and address not in address:
            addresses.append(address)
            continue

        if data == '-q':
            address = (address[0], address[1] + 1)
            addresses.remove(address)
            continue

        data = '%s: %s' % (address, data)

        for address in addresses:
            server.sendto(data, address)


if __name__ == '__main__':
    main()
