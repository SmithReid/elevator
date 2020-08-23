class Elevator(object):
    def __init__(self, starting_floor):
        self.doors_open = False
        self.current_floor = starting_floor
        self.relative_destination = 0 # destination relative to current_floor
        self.door_ticks = 0 # number of ticks with the doors open