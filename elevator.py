from request import Request

class Elevator(object):
    def __init__(self, recall_floor=0):
        self.requests = []
        self.recall_floor = recall_floor
        self.location = 0
        self.destination = 0
        self.doors_open = False
        self.doors_open_tick = -1
        self.active_request = Request(-1, 0, 0, -1, True, True)

    def move(self, tick_number):
        if self.location > self.destination: 
            self.location -= 1
        elif self.location < self.destination:
            self.location += 1
        if self.active_request.satisfied == False:
            if self.location == self.active_request.pickup \
                        and self.active_request.in_progress == False: 
                if self.doors_open == False: 
                    self.doors_open = True
                    self.doors_open_tick = tick_number
                else: 
                    if self.doors_open_tick <= tick_number - 3: 
                        self.doors_open = False
                        self.destination = self.active_request.destination
                        self.active_request.in_progress = True
            elif self.location == self.active_request.destination \
                        and self.active_request.in_progress == True:
                if self.doors_open == False: 
                    self.doors_open = True
                    self.doors_open_tick = tick_number
                else: 
                    if self.doors_open_tick <= tick_number - 3: 
                        self.doors_open = False
                        self.destination = self.recall_floor
                        self.active_request.satisfied = True
                        if len(self.requests) != 0: 
                            self.active_request = self.requests.pop()
                            import pdb
                            pdb.set_trace()

    def process_new_request(self, request):
        self.requests.append(request)
        if self.active_request.satisfied:
            self.active_request = self.requests.pop()
            self.destination = self.active_request.pickup