from floor import Floor
from elevator import Elevator
from sys import maxsize

class Manager(object):
    def __init__(self, n_floors, n_elevators, instructions, floors=[], elevators=[]):
        self.floors = []
        self.elevators = []
        self.requests = {}
        self.cleanup = False
        self.tick_number = 0
        if floors == [] and elevators == []:
            for i in range(n_floors):
                self.floors.append(Floor(i))
            for _ in range(n_elevators): 
                self.elevators.append(Elevator(0))
        else: 
            self.floors = floors
            self.elevators = elevators

    def tick(self):
        self._check_floors()
        self._schedule()
        for elevator in self.elevators:
            if elevator.doors_open == False:
                elevator.move()
            elif elevator.door_open_tick >= self.tick_number + 3:
                elevator.close_doors()

        self.tick_number += 1
        if self.tick_number == maxsize:
            self.tick_number = 0

        if self.cleanup: 
            return not bool(self.requests)
        return False
        
    def _schedule(self):
        for request in self.requests:
            pass

    def _check_floors(self):
        for i, floor in enumerate(self.floors):
            if floor.up_state == True:
                requests.update({{'direction': 'up', 'tick_called': self.tick_number, 'floor': floor.floor_number}})
            if floor.down_state == True:
                requests.update({{'direction': 'down', 'tick_called': self.tick_number, 'floor': floor.floor_number}})
            floor.clear_new_call()

    def end_run(self):
        self.cleanup = True

if __name__ == '__main__':
    pass