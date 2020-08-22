ffrom elevator import Elevator
from request import Request
from sys import maxsize

class Manager(object):
    def __init__(self, n_floors, n_elevators, instruction_filename):
        self.elevators = []
        self.requests = []
        self.cleanup = False

        self.instruction_filename = instruction_filename

        self.tick_number = 0
        self.request_id = 0

        for _ in range(n_elevators): 
            self.elevators.append(Elevator(0))

    def tick(self):
        print("Tick {}".format(str(self.tick_number)))
        for i, elevator in enumerate(self.elevators):
            print("Elevator {} on floor {}.".format(str(i), str(elevator.location)))
        self._parse_and_request()
        self._schedule()
        for elevator in self.elevators: 
            elevator.move(self.tick_number)

        self.tick_number += 1
        if self.tick_number == maxsize:
            self.tick_number = 0
            return not bool(self.requests)
        return False

    def _parse_and_request(self):
        with open(self.instruction_filename) as f: 
            requests = f.readlines()[self.tick_number].split(' ')
        for request in requests: 
            self.requests.append(Request(self.request_id, int(request[0]), int(request[1]), self.tick_number, False, False))
        
    def _schedule(self):
        for request in self.requests:
            self.elevators[0].process_new_request(request)

    def start_run(self):
        done = False
        while done == False:
            end = input()
            if end == 'end':
                self.end_run()
            done = self.tick()

    def end_run(self):
        self.cleanup = True

if __name__ == '__main__':
    pass