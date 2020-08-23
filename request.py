class Request(object):
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.elevator = -1 # Changes from -1 when an elevator is assigned