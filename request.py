class Request(object):
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.relative_destination = self.destination - self.origin
        self.elevator = -1 # Changes from -1 when an elevator is assigned

    def __repr__(self):
        return "(Request: {}, {})".format(self.origin, self.destination)