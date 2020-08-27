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
                self._move_elevator_as_necessary(elevator)
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
        This function takes a request as an input and assigns that request to an elevator
        
        At a more technical level, it checks each elevator for whether that elevator 
            is appropriate for this request, chooses the closest elevator going the 
            right way AND without too much distance to cover before satisfying the 
            newest request. 
        '''
        '''
        TODO: assign requests more evenly across elevators
        '''
        distance_to_elevator_from_origin = []
        for elevator in self.elevators:
            distance_to_elevator_from_origin.append(request.origin - elevator.current_floor)

        is_elevator_eligible = [True for elevator in self.elevators]

        # Eliminate elevators going in the wrong direction
        for i, distance in enumerate(distance_to_elevator_from_origin):
            if (request.relative_destination ^ distance) <= 0: 
            # if the elevator and the request are NOT going in the same direction: 
                is_elevator_eligible[i] = False

        possible_elevators = []
        
        for eligibility, elevator in zip(is_elevator_eligible, self.elevators):
            if eligibility and elevator.total_distance_all_requests < 20:
                possible_elevators.append(elevator)
        
        if possible_elevators:
            elevator_ids = []
            distances = []
            for elevator in possible_elevators:
                elevator_ids.append(elevator.id_num)
                distances.append(abs(elevator.current_floor - request.origin))

            request.elevator = elevator_ids[distances.index(min(distances))]

        else: 
            request.elevator = 1

        self.elevators[request.elevator].total_distance_all_requests += \
                    abs(request.destination - request.origin) + \
                    abs(self.elevators[request.elevator].current_floor - request.origin)
        self.active_requests.append(request)

    def _elevator_at_destination(self, elevator):
        if elevator.relative_destination == 0:
            pass

    def _move_elevator_as_necessary(self, elevator):
        if elevator.relative_destination > 0: 
            elevator.current_floor += 1
            elevator.relative_destination -= 1
        elif elevator.relative_destination < 0:
            elevator.current_floor -= 1
            elevator.relative_destination += 1










