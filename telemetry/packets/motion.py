from struct import unpack


class CarMotionData:
    def __init__(self, data):
        self.data = data
        self.car_motion_data = unpack('<ffffffHHHHHHffffff', data[24:84])