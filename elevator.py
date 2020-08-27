class Elevator(object):
    def __init__(self, id_num, starting_floor):
        self.id_num = id_num
        self.doors_open = False
        self.current_floor = starting_floor
        self.relative_destination = 0 # destination relative to current_floor
        self.door_ticks = 0 # number of ticks with the doors open
        self.total_distance_all_requests = 0

    def __repr__(self):
        return '\n(Elevator #{}\n'\
                'doors open?: {}\n'\
                'floor?: {}\n'\
                'relative_destination?: {}\n'\
                'door ticks?: {}\n'\
                'total distance to cover?: {}\n)'\
                .format(str(self.id_num), \
                    str(self.doors_open), \
                    str(self.current_floor), \
                    str(self.relative_destination), \
                    str(self.door_ticks), \
                    str(self.total_distance_all_requests))