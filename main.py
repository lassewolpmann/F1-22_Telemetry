from telemetry import collector, analyzer
import fastf1

fastf1.Cache.enable_cache('./cache')

if __name__ == '__main__':
    print('Starting Telemetry collection')
    print('Collection stops when Session is ended')
    telemetry = collector.receive_data()
    analyzer.analyze_data(telemetry)
