from floor import Floor
from elevator import Elevator
from sys import maxsize

class Manager(object):
    def __init__(self, n_floors, n_elevators, instruction_filename, \
            floors=[], elevators=[]):
        self.floors = []
        self.elevators = []
        self.requests = []
        self.cleanup = False

        self.instruction_filename = instruction_filename

        self.tick_number = 0
        self.request_id = 0

        if floors == [] and elevators == []:
            for i in range(n_floors):
                self.floors.append(Floor(i))
            for _ in range(n_elevators): 
                self.elevators.append(Elevator(0))
        else: 
            self.floors = floors
            self.elevators = elevators

    def tick(self, instructions=[]):
        self._parse_and_request(instructions)
        self._check_floors()
        self._schedule()
        self._process_elevators()

        self.tick_number += 1
        if self.tick_number == maxsize:
            self.tick_number = 0

        if self.cleanup: 
            return not bool(self.requests)
        return False

    def _parse_and_request(self, instructions):
        for instruction in instructions:
            if instruction[1] == 'u':
                self.floors[int(instruction[0])].new_up_call()
            elif instruction[1] == 'd':
                self.floors[int(instruction[0])].new_down_call()

    def _process_elevators(self):
        for elevator in self.elevators:
            if elevator.doors_open == False:
                elevator.move()
            elif elevator.door_open_tick >= self.tick_number + 3:
                elevator.close_doors()

            if elevator.destination == elevator.location:
                request_id = elevator.open_doors(self.tick_number)
                for request in self.requests:
                    if request['request_id'] == request_id:
                        del request

        
    def _schedule(self):
        for request in self.requests:
            import pdb
            pdb.set_trace()

    def _check_floors(self):
        for i, floor in enumerate(self.floors):
            if floor.up_state == True:
                self.requests.append({'direction': 'up', 'tick_called': self.tick_number, 'floor': floor.floor_number, 'scheduled': False, 'request_id': self.request_id})
                self.request_id += 1
            if floor.down_state == True:
                self.requests.append({'direction': 'down', 'tick_called': self.tick_number, 'floor': floor.floor_number, 'scheduled': False, 'request_id': self.request_id})
                self.request_id += 1
            floor.clear_new_call()

    def start_run(self):
        with open(self.instruction_filename) as f: 
                for line in f.readlines():
                    self.tick(line.split())

        done = False
        while done == False:
            end = input('tick {}'.format(self.tick_number))
            if end == 'end':
                self.end_run()
            done = self.tick()

    def end_run(self):
        self.cleanup = True

if __name__ == '__main__':
    pass