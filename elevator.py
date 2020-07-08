class Elevator(object):
    def __init__(self, recall_floor=False):
        self.location = 0
        self.destination = 0
        self.route = []
        self.recall_floor = recall_floor
        self.doors_open = False
        self.log = []
        self.request_log = []

    def recieve_request(self, request_id, pickup_floor):
        self.destination = pickup_floor
        self.request_log.append(request_id)
        self.request_id = request_id

    def move(self):
        if self.location > self.destination: 
            self.location -= 1
        elif self.location < self.destination:
            self.location += 1
        else: 
            if self.recall_floor:
                if self.location < self.recall_floor: 
                    self.location += 1
                elif self.location > self.recall_floor: 
                    self.location -= 1
        
    def open_doors(self, tick_number):
        self.doors_open = True
        self.door_open_tick = tick_number
        request_id = self.request_id
        del self.request_id
        return request_id

    def close_doors(self):
        self.doors_open = False
        del self.door_open_tick
        if len(self.route) != 0:
            self.destination = self.route.pop()