import json
import socket
from packets import car_telemetry, header, lap_data, event


def receive_data():
    UDP_IP = '127.0.0.1'
    UDP_PORT = 27001

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    telemetry = {}

    while True:
        data, addr = sock.recvfrom(2048)

        packet_id = header.PacketHeader(data).packet_id

        if packet_id == 0:
            # Motion Data
            pass

        elif packet_id == 1:
            # Session Data
            pass

        elif packet_id == 2:
            # Lap Data
            lap_time = lap_data.LapData(data).current_lap_ms
            lap_number = lap_data.LapData(data).current_lap

        elif packet_id == 3:
            # Event Data
            event_string_code = event.EventData(data).event_string_code

        elif packet_id == 4:
            # Participants
            pass

        elif packet_id == 5:
            # Car Setups
            pass

        elif packet_id == 6:
            # Telemetry Data
            speed = car_telemetry.CarTelemetryData(data).speed
            throttle = car_telemetry.CarTelemetryData(data).throttle
            steer = car_telemetry.CarTelemetryData(data).steer
            brake = car_telemetry.CarTelemetryData(data).brake
            gear = car_telemetry.CarTelemetryData(data).gear

            telemetry_data_received = True

        elif packet_id == 7:
            # Car Status
            pass

        elif packet_id == 8:
            # Final Classification
            pass

        elif packet_id == 9:
            # Lobby Info
            pass

        elif packet_id == 10:
            # Car Damage
            pass

        elif packet_id == 11:
            # Session History
            pass

        else:
            print('Packet ID wrong')

        if lap_time > 0:
            try:
                telemetry[f'Lap {lap_number}']

            except KeyError:
                telemetry[f'Lap {lap_number}'] = []

            telemetry[f'Lap {lap_number}'].append({
                'Lap Time': lap_time,
                'Speed': speed,
                'Throttle': throttle,
                'Steer': steer,
                'Brake': brake,
                'Gear': gear
            })

        if event_string_code == 'SEND':
            # Close Socket when Session ends
            break

    print('Session ended, writing data to telemetry.json')
    with open('telemetry.json', 'w') as outfile:
        json.dump(telemetry, outfile, indent=4)


if __name__ == '__main__':
    receive_data()
