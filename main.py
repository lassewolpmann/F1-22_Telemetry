import json
import socket
from packets import car_telemetry, header, lap_data, event, session_data


def receive_data():
    UDP_IP = '127.0.0.1'
    UDP_PORT = 27001

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    telemetry = {}
    lap_data_received = False
    telemetry_data_received = False

    while True:
        data, addr = sock.recvfrom(2048)

        packet_id = header.PacketHeader(data).packet_id

        if packet_id == 0:
            # Motion Data
            pass

        elif packet_id == 1:
            # Session Data
            track_length = session_data.SessionData(data).track_length

        elif packet_id == 2:
            # Lap Data
            lap_time = lap_data.LapData(data).current_lap_ms
            lap_number = lap_data.LapData(data).current_lap
            lap_distance = lap_data.LapData(data).lap_distance

            lap_data_received = True

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

        if lap_data_received and telemetry_data_received:
            if lap_time > 0 and lap_distance > 0:
                lap = f'Lap {lap_number}'

                try:
                    telemetry[lap]

                except KeyError:
                    telemetry[lap] = {}
                    telemetry[lap]['telemetry'] = []

                telemetry[lap]['telemetry'].append({
                    'Lap Time': lap_time,
                    'Lap Distance': lap_distance,
                    'Speed': speed,
                    'Throttle': throttle,
                    'Steer': steer,
                    'Brake': brake,
                    'Gear': gear
                })

                lap_data_received = False
                telemetry_data_received = False

        if event_string_code == 'SEND':
            # Close Socket when Session ends
            break

    print('Session ended, writing data to telemetry.json')
    for lap_key in telemetry.keys():
        lap_total_distance = telemetry[lap_key]['telemetry'][-1]['Lap Distance']

        if track_length - 5 < lap_total_distance < track_length + 5:
            telemetry[lap_key]['lap_completed'] = True

        else:
            telemetry[lap_key]['lap_completed'] = False

    with open('telemetry.json', 'w') as outfile:
        json.dump(telemetry, outfile, indent=4)


if __name__ == '__main__':
    receive_data()
