from struct import unpack


class SessionData:
    def __init__(self, data):
        self.data = data
        self.session_data = unpack('<BbbBHBbBHHBBBBBB', data[24:43])