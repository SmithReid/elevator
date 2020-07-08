class Floor(object):
    '''
    A 'new_call' is made when the user pushes the up or down button. The call is imported to the manager 1/tick and the new call is cleared before the light turns off when the elevator arrives
    '''

    def __init__(self, floor_number):
        self.up_state = False
        self.down_state = False
        self.doors_open = False
        self.new_call = False

        self.floor_number = floor_number

    def clear_new_call(self):
        self.up_state = False
        self.down_state = False
        self.new_call = False

    def new_up_call(self):
        self.up_state = True
        self.new_call = True

    def new_down_call(self):
        self.down_state = True
        self.new_call = True

    def open_doors(self):
        self.doors_open = True

    def close_doors(self):
        self.doors_open = False