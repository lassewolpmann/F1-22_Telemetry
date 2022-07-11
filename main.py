import socket
from struct import unpack


def receive_telemetry():
    UDP_IP = '127.0.0.1'
    UDP_PORT = 27001

    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)

    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(2048)

        header = unpack('<HBBBBQfIBB', data[0:24])
        packet_value = header[4]

        if packet_value == 0:
            # Motion Data
            m_carMotionData = unpack('<ffffffHHHHHHffffff', data[24:84])

        elif packet_value == 3:
            # Event Data
            m_eventStringCode = data[24:28]
            m_eventDetails = data[28:32]

        elif packet_value == 6:
            # Telemtry Data
            m_carTelemetryData = unpack('<HfffBbHBBHHBBHfB', data[24:57])
            print(m_carTelemetryData)


if __name__ == '__main__':
    receive_telemetry()
