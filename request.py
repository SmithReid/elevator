class Request(object):
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.relative_destination = self.destination - self.origin
        self.elevator = -1 # Changes from -1 when an elevator is assigned
        self.tick_active = 0

    def __repr__(self):
        return '\n(Request\n'\
                'floors: {}, {}\n'\
                'elevator: {}\n'\
                'relative_destination: {}\n'\
                .format(self.origin, self.destination, self.elevator, self.relative_destination)