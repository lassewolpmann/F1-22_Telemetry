import socket


def receive_telemetry():
    UDP_IP = '192.168.1.107'
    UDP_PORT = 20777

    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)

    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print("received message: %s" % data)


if __name__ == '__main__':
    receive_telemetry()
