class Request(object):
    def __init__(self, request_id, pickup, destination, tick_called, \
                        in_progress, satisfied):
        self.request_id = request_id
        self.pickup = pickup
        self.destination = destination
        self.tick_called = tick_called
        self.in_progress = in_progress
        self.satisfied = satisfied

    def __repr__(self):
        return 'request_id: ' + str(self.request_id) + '\n' + \
                'pickup: ' + str(self.pickup) + '\n' + \
                'destination: ' + str(self.destination) + '\n' + \
                'tick_called: ' + str(self.tick_called) + '\n' + \
                'in_progress: ' + str(self.in_progress) + '\n' + \
                'satisfied: ' + str(self.satisfied)
