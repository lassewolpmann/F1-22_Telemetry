from telemetry import collector, analyzer
import fastf1

fastf1.Cache.enable_cache('./cache')

if __name__ == '__main__':
    print('Starting Telemetry collection...')
    telemetry = collector.receive_data()
    analytics_choice: str = input('Do you want the data analyzed now? (y/n): ')

    if analytics_choice.lower() == 'y':
        analyzer.analyze_data(telemetry)

    elif analytics_choice.lower() == 'n':
        print('Data stored.')
        pass
