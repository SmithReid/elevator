from elevator import Elevator

class System(object):
    def __init__(self, parser, n_floors, n_elevators):
        self.parser = parser
        self.n_floors = n_floors
        self.elevators = []
        for _ in range(n_elevators): 
            self.elevators.append(Elevator(self.n_floors / 2))
        self.active_requests = []


    def tick(self, line):
        for request in line:
            import pdb
            pdb.set_trace()
        '''
        TODO: find the closest elevator going in the right direction
        TODO: assign request to that elevator
        TODO: determine which elevator to pass each request to and pass them
        TODO: move elevators, open doors, and close doors as appropriate
        TODO: check each active request and clear as appropriate
        '''

    def run(self):
        for line in self.parser.get_line():
            import pdb
            pdb.set_trace()
            self.tick(line)