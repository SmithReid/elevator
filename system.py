from elevator import Elevator

class System(object):
    def __init__(self, parser, n_floors, n_elevators):
        self.parser = parser
        self.n_floors = n_floors
        self.elevators = []
        for _ in n_elevators: 
            elevators.append(Elevator(self.n_floors / 2))
        self.active_requests = []


    def tick(self):
        self.parser.get_line()
        '''
        TODO: retrieve a tick of instructions from the parser
        TODO: determine which elevator to pass each request to and pass them
        TODO: move elevators, open doors, and close doors as appropriate
        TODO: check each active request and clear as appropriate
        '''