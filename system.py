from elevator import Elevator
from request import Request

class System(object):
    def __init__(self, parser, n_floors, n_elevators):
        self.parser = parser
        self.n_floors = n_floors
        self.elevators = []
        for i in range(n_elevators): 
            self.elevators.append(Elevator(i, self.n_floors // 2))
        self.active_requests = []


    def tick(self, line):
        for request_pair in line:
            request = Request(request_pair[0], request_pair[1])
            self._assign_request(request)

        for elevator in self.elevators:
            if elevator.relative_destination != 0:
                self._move_elevator(elevator)
            else: 
                self._elevator_at_destination(elevator)

        # TODO: stuff

        '''
        TODO: move elevators, open doors, and close doors as appropriate
        TODO: check each active request for completion and clear as appropriate
        '''

    def run(self):
        for line in self.parser.get_line():
            import pdb
            pdb.set_trace()
            self.tick(line)

    def _assign_request(self, request):
        '''
        TODO: assign requests more evenly across elevators
        '''
        distance_to_elevator_from_origin = []
        for elevator in self.elevators:
            distance_to_elevator_from_origin.append(request.origin - elevator.current_floor)

        is_elevator_going_right_way = [True for elevator in self.elevators]

        # Eliminate elevators going in the wrong direction
        for i, distance in enumerate(distance_to_elevator_from_origin):
            if (request.relative_destination ^ distance) < 0: 
            # if the elevator and the request are NOT going in the same direction: 
                is_elevator_going_right_way[i] = 0

        request.elevator = distance_to_elevator_from_origin.index(\
                                min(distance_to_elevator_from_origin))
        self.active_requests.append(request)

    def _elevator_at_destination(self, elevator):
        pass

    def _move_elevator(self, elevator):
        if elevator.relative_destination > 0: 
            elevator.current_floor += 1
        elif elevator.relative_destination < 0:
            elevator.current_floor -= 1








