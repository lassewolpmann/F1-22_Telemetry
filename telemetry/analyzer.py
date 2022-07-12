from matplotlib import pyplot as plt
import fastf1.plotting
import pandas as pd


def analyze_data(data):
    fastf1.plotting.setup_mpl()

    track = data['track_name']
    session = fastf1.get_session(2022, track, 'Q')

    session.load()
    driver = session.laps.pick_driver('LEC').pick_fastest()
    lec_car_data = driver.get_car_data()

    # Sort the laps by quickest time
    laps = data['laps']
    laps_sorted = sorted(laps, key=lambda k: len(laps[k]['telemetry']))

    fastest_lap_telemetry = None

    # Loop through laps, to find first fully completed lap
    for lap in laps_sorted:
        if data['laps'][lap]['lap_completed']:
            fastest_lap_telemetry = data['laps'][lap]['telemetry']
            break

        else:
            pass

    if fastest_lap_telemetry:
        # Setup Plot
        fig, ax = plt.subplots()

        # Plotting real fastest lap
        tLec = lec_car_data['Time']
        vCarLec = lec_car_data['Speed']
        ax.plot(tLec, vCarLec, label='Real Driver Lap', color='red')

        # Plotting own fastest lap
        t = pd.Series([pd.to_timedelta(data_point['Lap Time'], 'ms') for data_point in fastest_lap_telemetry])
        vCar = pd.Series([data_point['Speed'] for data_point in fastest_lap_telemetry])
        ax.plot(t, vCar, label='Own Lap', color='white')

        ax.set_xlabel('Time')
        ax.set_ylabel('Speed [Km/h]')
        ax.set_title(f'{session.event["EventName"]}, {session.name}')
        ax.legend()
        plt.show()

    else:
        print('No complete lap was recorded during this session')
