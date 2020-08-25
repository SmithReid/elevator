from request import Request

class Parser(object):
    def __init__(self, filename):
        with open(filename) as f:
            lines = f.readlines()
        self.instructions = [[[int(element) for element in request.split(' ')] for request in line.split(',')] for line in lines] # this was fun

    def get_line(self):
        for line in self.instructions:
            yield line