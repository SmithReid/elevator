from request import Request

class Parser(object):
    def __init__(self, filename):
        with open(filename) as f:
            lines = f.readlines()
        # TODO: split each line into requests
        # TODO: split each request into a tuple (origin, destination)


    def get_line(self):
        '''
        Parses a line and yields request objects
        '''
        for request in self.instructions[0]:
            yield Request(request)